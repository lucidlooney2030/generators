#!/usr/bin/env python3
"""
Coaxial three-layer Faraday generator v3 — analytical numeric sweep.
Orthodox physics only: E = -N dΦ/dt. No overunity.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent

# --- Magnet material (cited in PHYSICS.md) ---
BR_N42 = 1.30  # T typical mid-band
BR_N52 = 1.44  # T typical

# --- Geometry (m) ---
MAG_D_20 = 0.020
MAG_H = 0.005
MAG_D_3 = 0.003

# Preferred stack (mm→m): inner face r=28mm, gap 2, coil 9 radial, gap 2, outer face
R_INNER_FACE = 0.033
GAP = 0.002
COIL_RADIAL = 0.009
R_OUTER_FACE = R_INNER_FACE + GAP + COIL_RADIAL + GAP  # 0.041

AXIAL_ACTIVE = 0.022  # coil axial length ~ magnet diameter + margin


def magnet_area(d: float) -> float:
    return math.pi * (d / 2) ** 2


def max_poles_on_radius(r_face: float, mag_d: float, wall_mm: float = 3.0) -> int:
    """How many disc magnets fit around circumference with plastic wall between."""
    pitch = mag_d + wall_mm * 1e-3
    circ = 2 * math.pi * r_face
    return max(2, int(circ // pitch) // 2 * 2)  # even pole count


def bg_estimate(br: float, gap_total_m: float, dual: bool, magnet_len_m: float = MAG_H) -> float:
    """
    Crude reluctance estimate for radial gap between facing magnets.
    Dual magnets in series through air+coil path raise useful Bg vs single.
    Bg ≈ Br / (1 + μr_gap * g_eff / Lm_eff) with μr_gap~1, Lm_eff ~ 2*Lm for dual.
    """
    # Effective non-steel path: 2*gap + coil radial (plastic/copper ~ μ0)
    g_eff = gap_total_m + COIL_RADIAL
    lm = 2 * magnet_len_m if dual else magnet_len_m
    # Empirical leakage / fringing factor
    leak = 0.55 if dual else 0.40
    bg = br * (lm / (lm + g_eff)) * leak
    return max(0.05, min(bg, 0.9 * br))


def awg_diameter_m(awg: int) -> float:
    # Bare copper approx: d_mm = 0.127 * 92**((36-awg)/39)
    d_mm = 0.127 * (92 ** ((36 - awg) / 39))
    return d_mm * 1e-3


def coil_turns(awg: int, radial_m: float, axial_m: float, fill: float = 0.55) -> int:
    d = awg_diameter_m(awg)
    # With enamel approx +10%
    d_eff = d * 1.12
    n_rad = int(radial_m / d_eff)
    n_ax = int(axial_m / d_eff)
    return max(1, int(n_rad * n_ax * fill))


def mean_turn_length(r_inner_coil: float, r_outer_coil: float, axial: float) -> float:
    # Rectangular loop approx around radial thickness at mid radius
    r_mid = 0.5 * (r_inner_coil + r_outer_coil)
    # Each turn roughly: 2*axial + 2*(r_outer-r_inner) for a bobbin window? 
    # For cylindrical wall coil (axial solenoidal winding of radial flux machines),
    # use circumferential mean turn: 2π * r_mid (one turn around axis) — NO.
    # For radial-flux coaxial: coil is wound as multi-pole concentrated or distributed
    # windings in the annular wall. For simple concentrated coils (one per pole pair sector):
    # turn length ≈ 2*axial + 2*radial_span + end turns.
    radial_span = r_outer_coil - r_inner_coil
    sector_arc = 2 * math.pi * r_mid / 8  # assume 8 poles for length estimate; scaled later
    return 2 * axial + 2 * radial_span + 2 * sector_arc * 0.5


def resistance(n_turns: int, mean_len: float, awg: int, rho: float = 1.72e-8) -> float:
    d = awg_diameter_m(awg)
    a = math.pi * (d / 2) ** 2
    return rho * n_turns * mean_len / a


def phi_peak(bg: float, a_mag: float, k_c: float = 0.70) -> float:
    return k_c * bg * a_mag


def e_peak(n_turns: int, f_hz: float, phi: float) -> float:
    return n_turns * 2 * math.pi * f_hz * phi


def led_current(v_rms: float, r_coil: float, v_led: float = 2.0, r_series: float = 100.0) -> float:
    """Naive DC estimate after ideal bridge: Vdc~1.1*Vrms, through LED+series."""
    vdc = 1.1 * v_rms
    if vdc <= v_led:
        return 0.0
    r_tot = r_coil + r_series
    return (vdc - v_led) / r_tot


def compare_inner_choices():
    """Decide Ø20×5 vs Ø3×5 for inner drum."""
    rows = []
    for label, d_inner, dual in [
        ("outer20_inner20_dual", MAG_D_20, True),
        ("outer20_inner3_dual", MAG_D_3, True),
        ("outer20_only_single", MAG_D_20, False),
    ]:
        # Pole count limited by OUTER Ø20 on R_OUTER_FACE
        p_outer = max_poles_on_radius(R_OUTER_FACE, MAG_D_20, wall_mm=3.0)
        p_inner = max_poles_on_radius(R_INNER_FACE, d_inner, wall_mm=2.5 if d_inner < 0.01 else 3.0)
        p = min(p_outer, p_inner)
        if d_inner < 0.01:
            # small cans: can match outer pole count by placing cans at poles only
            p = p_outer
            a = magnet_area(d_inner)
        else:
            a = magnet_area(d_inner if dual else MAG_D_20)
        gap_total = 2 * GAP
        bg = bg_estimate(BR_N42, gap_total, dual=dual)
        # For single (no inner), use outer only area
        if not dual:
            a = magnet_area(MAG_D_20)
        phi = phi_peak(bg, a, k_c=0.70 if dual else 0.55)
        # figure of merit at fixed RPM: E ~ N * f * Φ ~ P * Φ (N fixed)
        fom = p * phi
        rows.append(dict(label=label, P=p, Bg=bg, A=a, Phi=phi, FoM_P_Phi=fom, dual=dual))
    return rows


def run_sweep():
    decisions = compare_inner_choices()
    # Pick best FoM
    best = max(decisions, key=lambda r: r["FoM_P_Phi"])
    chosen_inner = MAG_D_20 if "inner20" in best["label"] else MAG_D_3
    dual = best["dual"]

    pole_counts = [6, 8, 10]
    gaps_mm = [1.0, 2.0, 3.0]
    awgs = [28, 26]
    rpms = np.arange(60, 601, 30)
    inner_options = [
        ("inner_D20x5", MAG_D_20),
        ("inner_D3x5", MAG_D_3),
    ]

    csv_path = OUT / "sweep_results.csv"
    fields = [
        "inner_choice", "P", "gap_mm", "AWG", "N_turns", "R_coil_ohm",
        "Bg_T", "Phi_Wb", "RPM", "f_Hz", "Voc_peak_V", "Voc_rms_V",
        "I_led_mA", "FoM",
    ]
    rows_out = []

    r_coil_i = R_INNER_FACE + 0.002  # nominal for R estimate; adjusted per gap in loop
    for inner_label, d_in in inner_options:
        for P in pole_counts:
            # Feasibility: outer must fit P × Ø20
            if max_poles_on_radius(R_OUTER_FACE, MAG_D_20, 3.0) < P:
                continue
            if d_in >= 0.015 and max_poles_on_radius(R_INNER_FACE, d_in, 3.0) < P:
                continue
            for gap_mm in gaps_mm:
                gap = gap_mm * 1e-3
                r_ci = R_INNER_FACE + gap
                r_co = r_ci + COIL_RADIAL
                # outer face moves with gap (keep coil fixed thickness, outer radius shifts)
                # For model: fix inner face & coil; outer face = r_co + gap
                bg = bg_estimate(BR_N42, 2 * gap, dual=True)
                a = magnet_area(d_in)  # facing pair limited by smaller magnet
                # When inner is small, flux limited by inner area; outer still helps return
                phi = phi_peak(bg, a, k_c=0.70)
                for awg in awgs:
                    n = coil_turns(awg, COIL_RADIAL, AXIAL_ACTIVE, fill=0.55)
                    # Total series turns across all pole coils (P/2 coil groups × turns) —
                    # simple single-phase: wind P concentrated coils in series
                    n_total = n  # turns in the winding window (shared bobbin wall)
                    # For multi-pole, flux linkage uses N per coil; series P/2 active at peak
                    # Conservative: use N_total as bobbin turns, Φ per magnet face
                    mean_len = 2 * AXIAL_ACTIVE + 2 * COIL_RADIAL + (2 * math.pi * 0.5 * (r_ci + r_co) / P)
                    # Scale: each turn links one pole face; P coils in series → multiply N by P? 
                    # Standard: distributed wall with N turns total linking alternating flux.
                    # Use N_series = n_total (one long winding); effective poles enter via f.
                    r_coil = resistance(n_total, mean_len * P, awg)  # P sectors chain
                    for rpm in rpms:
                        f = (rpm / 60.0) * (P / 2.0)
                        ep = e_peak(n_total, f, phi)
                        # series connection of pole coils boosts voltage ~P/2 active additive
                        # Use factor: concentrated coils in series → ~ (P/2) * E_one at peak alignment
                        # Conservative series factor:
                        series_factor = max(1.0, P / 2.0 * 0.85)
                        ep *= series_factor
                        er = ep / math.sqrt(2)
                        i_led = led_current(er, r_coil)
                        rows_out.append({
                            "inner_choice": inner_label,
                            "P": P,
                            "gap_mm": gap_mm,
                            "AWG": awg,
                            "N_turns": n_total,
                            "R_coil_ohm": round(r_coil, 2),
                            "Bg_T": round(bg, 4),
                            "Phi_Wb": f"{phi:.4e}",
                            "RPM": int(rpm),
                            "f_Hz": round(f, 3),
                            "Voc_peak_V": round(ep, 3),
                            "Voc_rms_V": round(er, 3),
                            "I_led_mA": round(i_led * 1e3, 2),
                            "FoM": round(P * phi * n_total, 6),
                        })

    with csv_path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows_out)

    # Baseline recommended: inner20, P=8, gap=2, AWG26
    base = [r for r in rows_out
            if r["inner_choice"] == "inner_D20x5" and r["P"] == 8
            and r["gap_mm"] == 2.0 and r["AWG"] == 26]
    base3 = [r for r in rows_out
             if r["inner_choice"] == "inner_D3x5" and r["P"] == 8
             and r["gap_mm"] == 2.0 and r["AWG"] == 26]

    # Plot Voc vs RPM
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([r["RPM"] for r in base], [r["Voc_rms_V"] for r in base], "b-o", label="Ø20 inner dual, P=8, 2mm, 26AWG")
    ax.plot([r["RPM"] for r in base3], [r["Voc_rms_V"] for r in base3], "r--s", label="Ø3 inner dual, P=8, 2mm, 26AWG")
    ax.set_xlabel("RPM")
    ax.set_ylabel("Voc rms (V)")
    ax.set_title("Coax Faraday v3 — open-circuit voltage vs RPM")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "voc_vs_rpm.png", dpi=140)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot([r["RPM"] for r in base], [r["I_led_mA"] for r in base], "b-o", label="Ø20 inner")
    ax.plot([r["RPM"] for r in base3], [r["I_led_mA"] for r in base3], "r--s", label="Ø3 inner")
    ax.set_xlabel("RPM")
    ax.set_ylabel("Est. LED current (mA) via 100Ω + 2V LED")
    ax.set_title("Coax Faraday v3 — estimated LED current vs RPM")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "iled_vs_rpm.png", dpi=140)
    plt.close(fig)

    # Gap sweep at 120 RPM
    gap_rows = [r for r in rows_out
                if r["inner_choice"] == "inner_D20x5" and r["P"] == 8
                and r["AWG"] == 26 and r["RPM"] == 120]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot([r["gap_mm"] for r in gap_rows], [r["Voc_rms_V"] for r in gap_rows], "g-o")
    ax.set_xlabel("Air gap each side (mm)")
    ax.set_ylabel("Voc rms @ 120 RPM (V)")
    ax.set_title("Gap sensitivity — Ø20 dual, P=8, 26AWG")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "voc_vs_gap.png", dpi=140)
    plt.close(fig)

    # Summary JSON-ish text
    at120 = next(r for r in base if r["RPM"] == 120)
    at120_3 = next(r for r in base3 if r["RPM"] == 120)
    summary = OUT / "sim_summary.txt"
    summary.write_text(
        f"""Coax Faraday v3 simulation summary
=====================================
Magnet grade assumption: N42, Br={BR_N42} T (N52 Br={BR_N52} optional)
Geometry: R_inner_face={R_INNER_FACE*1e3:.1f} mm, coil_radial={COIL_RADIAL*1e3:.1f} mm, R_outer_face≈{R_OUTER_FACE*1e3:.1f} mm

Inner magnet decision candidates:
"""
        + "\n".join(
            f"  {d['label']}: P={d['P']}, Bg={d['Bg']:.3f} T, Phi={d['Phi']:.4e} Wb, FoM=P*Phi={d['FoM_P_Phi']:.4e}"
            for d in decisions
        )
        + f"""

CHOSEN: Ø20×5 mm discs on BOTH inner and outer (dual facing).
Reason: FoM (P·Φ) dominates; Ø3 area is (3/20)^2 ≈ 2.25% → voltage collapses despite same P.
Topology: outer+inner magnet drums locked as one rotor; coil cylinder fixed stator.

Baseline @ 120 RPM (P=8, gap=2 mm, 26 AWG):
  Voc_rms ≈ {at120['Voc_rms_V']} V, Voc_peak ≈ {at120['Voc_peak_V']} V
  f = {at120['f_Hz']} Hz, N≈{at120['N_turns']}, R≈{at120['R_coil_ohm']} Ω
  LED current est ≈ {at120['I_led_mA']} mA (100 Ω series, 2 V LED, after naive bridge)

Ø3 inner same conditions @ 120 RPM:
  Voc_rms ≈ {at120_3['Voc_rms_V']} V, I_led ≈ {at120_3['I_led_mA']} mA

CSV: {csv_path}
Plots: voc_vs_rpm.png, iled_vs_rpm.png, voc_vs_gap.png
""",
        encoding="utf-8",
    )
    print(summary.read_text())
    return at120


if __name__ == "__main__":
    run_sweep()
