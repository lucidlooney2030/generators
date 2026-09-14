#!/usr/bin/env python3
"""
AFPM-Desk-v4 PoleShoe — analytical Voc vs RPM sanity check.
Orthodox physics only: E = -N dΦ/dt. No overunity / free energy.
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

BR_N42 = 1.30  # T mid-band
MAG_D = 0.020
MAG_H = 0.005
P = 12
AM = math.pi * (MAG_D / 2) ** 2
GAP = 0.00175
COIL_AXIAL = 0.010
N_HAND = 200          # recommended hand-wind target (28 AWG)
AWG = 28
MEAN_TURN = 2 * (0.024 + 0.016)  # bobbin rectangle


def bg_estimate(br: float = BR_N42, gap: float = GAP, with_shoes: bool = True,
                mag_h: float = MAG_H) -> float:
    """Crude SSDR reluctance model with back-iron (+ optional pole shoes)."""
    g_eff = 2 * gap + COIL_AXIAL
    lm = 2 * mag_h
    leak = 0.62 if with_shoes else 0.55
    leak += 0.03  # steel back-iron
    bg = br * (lm / (lm + g_eff)) * leak
    return max(0.05, min(bg, 0.85 * br))


def awg_diameter_m(awg: int) -> float:
    return 0.127 * (92 ** ((36 - awg) / 39)) * 1e-3


def resistance(n: int, mean_len: float, awg: int, rho: float = 1.72e-8) -> float:
    d = awg_diameter_m(awg)
    a = math.pi * (d / 2) ** 2
    return rho * n * mean_len / a


def phi_peak(bg: float, kc: float = 0.70) -> float:
    return kc * bg * AM


def freq(rpm: float, poles: int = P) -> float:
    return (rpm / 60.0) * (poles / 2.0)


def e_rms(n: int, f: float, phi: float) -> float:
    return (n * 2 * math.pi * f * phi) / math.sqrt(2)


def main():
    bg_shoes = bg_estimate(with_shoes=True)
    bg_noshoe = bg_estimate(with_shoes=False)
    bg_v2 = bg_estimate(with_shoes=False, mag_h=0.003)  # thinner mags, no shoes

    # Slightly higher "optimistic teaching" Bg if shoes concentrate (upper band)
    bg_opt = min(0.70, bg_shoes * 1.35)

    phi = phi_peak(bg_shoes)
    phi_opt = phi_peak(bg_opt)
    n = N_HAND
    r_coil = resistance(n, MEAN_TURN, AWG)

    rpms = np.arange(60, 181, 10)
    rows = []
    for rpm in rpms:
        f = freq(float(rpm))
        voc1 = e_rms(n, f, phi)
        voc1o = e_rms(n, f, phi_opt)
        voc_ph = 3 * voc1
        voc_ll = voc_ph * math.sqrt(3)
        rows.append({
            "rpm": int(rpm),
            "f_hz": round(f, 2),
            "voc_1coil_rms": round(voc1, 3),
            "voc_1coil_opt_rms": round(voc1o, 3),
            "voc_phase_3series_rms": round(voc_ph, 3),
            "voc_line_Y_rms": round(voc_ll, 3),
            "bg_T": round(bg_shoes, 3),
            "phi_Wb": f"{phi:.3e}",
            "N": n,
            "R_coil_ohm": round(r_coil, 2),
        })

    with (OUT / "sweep_results.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot([r["rpm"] for r in rows], [r["voc_1coil_rms"] for r in rows], "o-", label="1 coil (conservative Bg)")
    ax.plot([r["rpm"] for r in rows], [r["voc_1coil_opt_rms"] for r in rows], "--", label="1 coil (upper Bg band)")
    ax.plot([r["rpm"] for r in rows], [r["voc_phase_3series_rms"] for r in rows], "s-", label="1 phase (3 series)")
    ax.plot([r["rpm"] for r in rows], [r["voc_line_Y_rms"] for r in rows], "^-", label="Y line-line")
    ax.set_xlabel("RPM")
    ax.set_ylabel("Voc rms (V)")
    ax.set_title(f"AFPM-Desk-v4 PoleShoe — Voc vs RPM (N={n}, {AWG} AWG)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "voc_vs_rpm.png", dpi=120)
    plt.close()

    gaps = np.linspace(0.0010, 0.0030, 9)
    gap_rows = []
    for g in gaps:
        bg = bg_estimate(gap=float(g), with_shoes=True)
        ph = phi_peak(bg)
        voc1 = e_rms(n, freq(120), ph)
        gap_rows.append((g * 1e3, bg, voc1, 3 * voc1))

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot([g[0] for g in gap_rows], [g[3] for g in gap_rows], "o-")
    ax.set_xlabel("Air gap each side (mm)")
    ax.set_ylabel("Phase Voc rms @ 120 RPM (V)")
    ax.set_title("v4 PoleShoe — gap sensitivity (3 coils/phase, N=200)")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "voc_vs_gap.png", dpi=120)
    plt.close()

    r120 = next(r for r in rows if r["rpm"] == 120)
    summary = f"""AFPM-Desk-v4 PoleShoe sim summary
================================
Assumptions: N42 Br={BR_N42} T, P={P}, gap={GAP*1e3:.2f} mm/side, coil axial={COIL_AXIAL*1e3:.0f} mm
Bg with pole shoes+back-iron (conservative): {bg_shoes:.3f} T
Bg without shoes (steel only): {bg_noshoe:.3f} T
Bg v2-like (3 mm mag, no shoes): {bg_v2:.3f} T
Bg upper teaching band (shoes): {bg_opt:.3f} T
Phi_peak (conservative): {phi:.3e} Wb
Turns/coil ({AWG} AWG hand target): {n}, R≈{r_coil:.1f} Ω

@ 120 RPM: f={r120['f_hz']} Hz
  Voc 1 coil rms (cons.): {r120['voc_1coil_rms']} V
  Voc 1 coil rms (upper): {r120['voc_1coil_opt_rms']} V
  Voc phase (3 ser):      {r120['voc_phase_3series_rms']} V
  Voc Y line-line:        {r120['voc_line_Y_rms']} V

Order-of-magnitude @ 120 RPM: ~0.8–3 Vrms / coil; ~2–8 Vrms / phase; LED-scale after rectification.
NOT free energy — mechanical work against Lenz drag supplies the power.
"""
    (OUT / "sim_summary.txt").write_text(summary)
    print(summary)


if __name__ == "__main__":
    main()
