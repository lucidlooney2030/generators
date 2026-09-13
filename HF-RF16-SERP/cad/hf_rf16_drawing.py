#!/usr/bin/env python3
"""HF-RF16-SERP fully dimensioned drawing → PDF + PNG."""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
import numpy as np

from hf_rf16_params import *
from hf_rf16_params import summary
from hf_rf16_params import STEEL_STRIP

OUT = Path(__file__).resolve().parent
TITLE = "HF-RF16-SERP  16P/16S  radial flux outer rotor, single-phase wave winding."


def _style(ax):
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.25, linewidth=0.4)
    ax.tick_params(labelsize=7)


def fig_axial_section(fig, ax):
    """Axial cross-section with 1.00 air-gap callout."""
    ax.set_title("Axial cross-section (radial stack-up)", fontsize=10, pad=8)

    # Draw half-section from axis outward as rectangles in R-Z
    # Horizontal = R, Vertical = Z
    z_floor = 0
    z_int = ROTOR_FLOOR
    z_rim = ROTOR_CUP_H
    z_pcl = ROTOR_FLOOR + POCKET_CL_FROM_FLOOR

    # Rotor outer wall
    ax.add_patch(patches.Rectangle((BACKIRON_R_OUT, z_floor), ROTOR_OR - BACKIRON_R_OUT, z_rim - z_floor,
                                   facecolor="#6b8cae", edgecolor="k", lw=0.6, label="rotor"))
    # Rotor floor
    ax.add_patch(patches.Rectangle((0, z_floor), ROTOR_OR, ROTOR_FLOOR,
                                   facecolor="#6b8cae", edgecolor="k", lw=0.6))
    # Back iron strip
    ax.add_patch(patches.Rectangle((BACKIRON_R_IN, z_pcl - BACKIRON_AXIAL/2),
                                   BACKIRON_R_OUT - BACKIRON_R_IN, BACKIRON_AXIAL,
                                   facecolor="#888", edgecolor="k", lw=0.5, label="steel strip"))
    # Magnet
    ax.add_patch(patches.Rectangle((MAG_FACE_R, z_pcl - MAG_DIA/2),
                                   MAG_THK, MAG_DIA,
                                   facecolor="#c44", edgecolor="k", lw=0.6, label="NdFeB"))
    # Air gap band
    ax.add_patch(patches.Rectangle((SLEEVE_OUTER_R, z_pcl - 11),
                                   AIR_GAP, 22,
                                   facecolor="#ffe680", edgecolor="#ca0", lw=0.8, label="air gap 1.00"))
    # Sleeve
    ax.add_patch(patches.Rectangle((SLEEVE_INNER_R, z_pcl - SLEEVE_AXIAL/2),
                                   SLEEVE_WALL, SLEEVE_AXIAL,
                                   facecolor="#9c6", edgecolor="k", lw=0.5, label="sleeve"))
    # Stator body (bore to groove floor)
    st_z0 = z_pcl - GROOVE_AXIAL/2 - GALLERY_AXIAL
    ax.add_patch(patches.Rectangle((BORE_R, st_z0), GROOVE_FLOOR_R - BORE_R, STATOR_AXIAL,
                                   facecolor="#d4a574", edgecolor="k", lw=0.6, label="stator"))
    # Stator land / groove region (simplified land)
    ax.add_patch(patches.Rectangle((GROOVE_FLOOR_R, z_pcl - GROOVE_AXIAL/2),
                                   GROOVE_OUTER_R - GROOVE_FLOOR_R, GROOVE_AXIAL,
                                   facecolor="#e8c9a0", edgecolor="k", lw=0.4))
    # Copper fill indicator
    ax.add_patch(patches.Rectangle((GROOVE_FLOOR_R, z_pcl - GROOVE_AXIAL/2),
                                   COPPER_FILL, GROOVE_AXIAL,
                                   facecolor="#daa520", alpha=0.45, edgecolor="none", label="copper ~5.58"))
    # Steel tube
    ax.add_patch(patches.Rectangle((BORE_R - STEEL_TUBE_WALL, st_z0),
                                   STEEL_TUBE_WALL, STEEL_TUBE_LEN,
                                   facecolor="#555", edgecolor="k", lw=0.5, label="steel tube"))
    # Shaft
    ax.add_patch(patches.Rectangle((0, -5), SHAFT_D/2, 50,
                                   facecolor="#bbb", edgecolor="k", lw=0.4))
    # Cap
    ax.add_patch(patches.Rectangle((0, st_z0 + STATOR_AXIAL), GROOVE_OUTER_R + 3, CAP_THK,
                                   facecolor="#a8c4a0", edgecolor="k", lw=0.5))

    # Dimension callouts
    y_dim = -8
    def dim_h(x0, x1, y, text, dy=-3):
        ax.annotate("", xy=(x1, y), xytext=(x0, y),
                    arrowprops=dict(arrowstyle="<->", color="k", lw=0.7))
        ax.text((x0+x1)/2, y+dy, text, ha="center", va="top", fontsize=6)

    dim_h(0, BORE_R, y_dim, f"bore r={BORE_R:.2f}", -2.5)
    dim_h(GROOVE_FLOOR_R, SLEEVE_INNER_R, y_dim - 6, f"Cu fill {COPPER_FILL:.2f}", -2.5)
    dim_h(SLEEVE_OUTER_R, MAG_FACE_R, y_dim - 12, f"AG {AIR_GAP:.2f}", -2.5)
    dim_h(MAG_FACE_R, MAG_BACK_R, y_dim - 6, f"mag {MAG_THK:.1f}", -2.5)
    dim_h(0, ROTOR_OR, y_dim - 18, f"rotor OD/2={ROTOR_OR:.1f}", -2.5)

    # Vertical labels
    ax.text(MAG_FACE_R + 0.2, z_pcl + MAG_DIA/2 + 1.5, "magnet face r=56.38", fontsize=6, color="#a00")
    ax.text(SLEEVE_OUTER_R - 0.2, z_pcl + 12, "sleeve OR 55.38", fontsize=6, ha="right", color="#060")
    ax.text(GROOVE_FLOOR_R + 0.2, st_z0 + 1, "groove floor r=49.00", fontsize=6, color="#840")
    ax.text(BORE_R + 0.3, st_z0 + STATOR_AXIAL - 2, "printed wall 2.00", fontsize=6, color="#840")

    ax.set_xlim(-2, ROTOR_OR + 5)
    ax.set_ylim(-22, z_rim + 12)
    ax.set_xlabel("radius r (mm)", fontsize=8)
    ax.set_ylabel("axial z (mm)", fontsize=8)
    ax.legend(loc="upper right", fontsize=6, framealpha=0.9)
    _style(ax)


def fig_rotor_polar(fig, ax):
    ax.set_title("Rotor polar layout — 16×22.5° magnet pockets", fontsize=10)
    ax.set_xlim(-70, 70)
    ax.set_ylim(-70, 70)
    # OD
    ax.add_patch(patches.Circle((0, 0), ROTOR_OR, fill=False, lw=1.2, color="k"))
    ax.add_patch(patches.Circle((0, 0), BACKIRON_R_OUT, fill=False, lw=0.6, color="#666", ls="--"))
    ax.add_patch(patches.Circle((0, 0), MAG_BACK_R, fill=False, lw=0.5, color="#888"))
    ax.add_patch(patches.Circle((0, 0), MAG_FACE_R, fill=False, lw=0.8, color="#c44"))
    ax.add_patch(patches.Circle((0, 0), MAG_FACE_R - LIP_THK, fill=False, lw=0.5, color="#6b8cae"))

    for i in range(MAG_COUNT):
        a = math.radians(i * PITCH_DEG)
        # Magnet rectangle in polar: center at face+thk/2
        rc = MAG_FACE_R + MAG_THK / 2
        cx, cy = rc * math.cos(a), rc * math.sin(a)
        # Draw as circle for pocket
        ax.add_patch(patches.Circle((cx, cy), MAG_DIA / 2, fill=True,
                                    facecolor=("#c44" if i % 2 == 0 else "#448"),
                                    edgecolor="k", lw=0.4, alpha=0.85))
        # Polarity label
        ax.text(cx, cy, "N" if i % 2 == 0 else "S", ha="center", va="center",
                fontsize=6, color="w", fontweight="bold")
        # Angle tick
        ax.plot([0, ROTOR_OR * math.cos(a)], [0, ROTOR_OR * math.sin(a)],
                color="#ccc", lw=0.3)

    ax.text(0, -ROTOR_OR - 4, "N-S-N-S alternate · pitch 22.50° · face pitch radius 56.38",
            ha="center", fontsize=7)
    ax.text(0, ROTOR_OR + 3, f"OD {ROTOR_OD:.0f}  ·  back-iron groove r={BACKIRON_R_IN}–{BACKIRON_R_OUT}",
            ha="center", fontsize=7)
    ax.axis("off")
    _style(ax)


def fig_unrolled(fig, ax):
    ax.set_title("Unrolled 16-slot square-wave / serpentine winding", fontsize=10)
    n = MAG_COUNT
    slot_w = 1.0
    xs = np.arange(n + 1)

    # Magnets above
    for i in range(n):
        color = "#c44" if i % 2 == 0 else "#448"
        ax.add_patch(patches.Rectangle((i, 3.2), 0.9, 0.7, facecolor=color, edgecolor="k", lw=0.4))
        ax.text(i + 0.45, 3.55, "N" if i % 2 == 0 else "S", ha="center", va="center",
                fontsize=7, color="w", fontweight="bold")

    # Grooves
    for i in range(n):
        ax.add_patch(patches.Rectangle((i + 0.15, 0.5), 0.6, 2.4, fill=False, lw=0.8, color="#840"))
        ax.text(i + 0.45, 0.25, f"g{i+1}", ha="center", fontsize=6)

    # Serpentine path: up odd, down even
    # g1 bottom→top, gallery to g2, top→bottom, ...
    path_x = []
    path_y = []
    for i in range(n):
        x = i + 0.45
        if i % 2 == 0:
            # up
            path_x += [x, x]
            path_y += [0.6, 2.8]
        else:
            path_x += [x, x]
            path_y += [2.8, 0.6]
        # gallery over to next
        if i < n - 1:
            x2 = i + 1 + 0.45
            if i % 2 == 0:
                # top gallery
                path_x += [x, x2]
                path_y += [2.8, 2.8]
            else:
                path_x += [x, x2]
                path_y += [0.6, 0.6]
    # return slot to g1 bottom
    path_x += [n - 1 + 0.45, n + 0.2, n + 0.2, 0.45]
    path_y += [0.6, 0.6, 0.15, 0.15]

    ax.plot(path_x, path_y, color="#daa520", lw=2.0, solid_capstyle="round")
    # Arrows on axial runs
    for i in range(n):
        x = i + 0.45
        if i % 2 == 0:
            ax.annotate("", xy=(x, 2.5), xytext=(x, 1.0),
                        arrowprops=dict(arrowstyle="->", color="#333", lw=1.2))
        else:
            ax.annotate("", xy=(x, 1.0), xytext=(x, 2.5),
                        arrowprops=dict(arrowstyle="->", color="#333", lw=1.2))

    ax.text(n / 2, 4.2, "Magnets (rotor) — polarity above axial runs · serpentine pitch = pole pitch = 22.5°",
            ha="center", fontsize=7)
    ax.text(n / 2, -0.3, "26 AWG wave winding · target 80–120 turns · tails out cap · bridge + ≥1000 µF",
            ha="center", fontsize=7)
    ax.set_xlim(-0.5, n + 1.5)
    ax.set_ylim(-0.6, 4.6)
    ax.axis("off")


def fig_bom_table(fig, ax):
    ax.axis("off")
    ax.set_title("Hardware BOM (bought) + key printed parts", fontsize=10)
    rows = [
        ["Qty", "Item", "Notes"],
        ["16", "NdFeB Ø20×5", "axially magnetized, N-S alt."],
        ["1", "Steel strip 1.50×20.00×386", "mild steel back-iron"],
        ["1", "Steel tube OD≈94 wall~3 L~28", "flux return (bore Ø94)"],
        ["2", "608ZZ bearing", "22×8×7"],
        ["1", "Shaft Ø8", "through both bearings"],
        ["—", "M3 screws / heat-set inserts", "rotor 6×; stator/cap 4×"],
        ["—", "M2 or snaps", "sleeve clips"],
        ["1 spool", "26 AWG magnet wire", "serpentine 80–120 turns"],
        ["4", "Diodes (bridge)", "full-wave rectifier"],
        ["1", "Capacitor ≥1000 µF", "DC filter"],
        ["1", "HF-RF16-ROTOR.stl", "PETG/ABS/ASA/nylon"],
        ["1", "HF-RF16-STATOR.stl", "grooves UP"],
        ["1", "HF-RF16-SLEEVE.stl", "2×180° shells"],
        ["1", "HF-RF16-CAP.stl", "bearing + grommets"],
    ]
    table = ax.table(cellText=rows[1:], colLabels=rows[0], loc="center", cellLoc="left")
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.0, 1.25)
    for (r, c), cell in table.get_celld().items():
        if r == 0:
            cell.set_facecolor("#333")
            cell.set_text_props(color="w", fontweight="bold")
        elif r % 2 == 0:
            cell.set_facecolor("#f0f0f0")


def fig_dims_table(fig, ax):
    ax.axis("off")
    ax.set_title("Key dimensions (mm) — resolved geometry", fontsize=10)
    s = summary()
    rows = [["Parameter", "Value"]]
    labels = [
        ("MAG_COUNT", "16"),
        ("Pole/slot pitch", "22.50°"),
        ("Magnet face radius", f"{MAG_FACE_R:.2f}"),
        ("Magnet back radius", f"{MAG_BACK_R:.2f}"),
        ("Air gap", f"{AIR_GAP:.2f}"),
        ("Sleeve outer / inner r", f"{SLEEVE_OUTER_R:.2f} / {SLEEVE_INNER_R:.2f}"),
        ("Bore diameter (radius)", f"{BORE_D:.2f} ({BORE_R:.2f})"),
        ("Groove floor radius", f"{GROOVE_FLOOR_R:.2f}"),
        ("Printed wall bore→floor", f"{PRINTED_WALL:.2f}"),
        ("Copper radial fill", f"{COPPER_FILL:.2f}"),
        ("Groove / land arc @55.38", f"{GROOVE_W:.2f} / {LAND_W:.2f}"),
        ("Rotor OD", f"{ROTOR_OD:.2f}"),
        ("Steel strip cut length", f"{STEEL_STRIP[2]}"),
    ]
    for a, b in labels:
        rows.append([a, b])
    table = ax.table(cellText=rows[1:], colLabels=rows[0], loc="center", cellLoc="left")
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.0, 1.35)
    for (r, c), cell in table.get_celld().items():
        if r == 0:
            cell.set_facecolor("#1a4")
            cell.set_text_props(color="w", fontweight="bold")


def fig_conflict(fig, ax):
    ax.axis("off")
    ax.set_title("Geometry conflict resolution", fontsize=10)
    text = (
        "CONFLICT: Original notes had drum bore r=47.00 with groove floor r=47.38,\n"
        "leaving only 0.38 mm printed wall (below the ≥2.00 mm minimum). Copper fill\n"
        "quoted as ~7.2 mm was inconsistent with a corrected sleeve outer r=55.38.\n\n"
        "RESOLUTION (preferred):\n"
        "  • Magnet face r = 56.38, air gap = 1.00 exactly (≤1.2).\n"
        "  • Sleeve OUTER r = 55.38, wall = 0.80 → INNER r = 54.58.\n"
        "  • Bore RADIUS = 47.00 (diameter 94.00) for steel flux-return tube OD≈94.\n"
        "  • Groove floor r = 49.00 → printed wall = 2.00 mm.\n"
        "  • Copper radial fill = 55.38 − 0.80 − 49.00 = 5.58 mm (revises “7.2”).\n"
        "  • Groove open at r=55.38 before sleeve; land/groove arcs 9.75 / 12.00 at\n"
        "    that radius sum to pitch arc 21.75 mm (16×22.5°) — no ±0.5 adjustment needed.\n"
        "  • Legacy BOM “steel tube OD~47” referred to the bore RADIUS figure; corrected\n"
        "    tube OD≈94 mm wall~3 length~28 to match Ø94 bore.\n"
    )
    ax.text(0.02, 0.98, text, va="top", ha="left", fontsize=8, family="monospace",
            transform=ax.transAxes)


def main():
    pdf_path = OUT / "HF-RF16-DRAWING.pdf"
    png_path = OUT / "HF-RF16-DRAWING.png"

    with PdfPages(pdf_path) as pdf:
        # Page 1: title + axial + polar
        fig = plt.figure(figsize=(11, 8.5))
        fig.suptitle(TITLE, fontsize=11, fontweight="bold", y=0.98)
        ax1 = fig.add_axes([0.05, 0.08, 0.55, 0.82])
        fig_axial_section(fig, ax1)
        ax2 = fig.add_axes([0.58, 0.35, 0.40, 0.55])
        fig_rotor_polar(fig, ax2)
        fig.text(0.72, 0.12, "Austin Carolino  ·  units mm  ·  NOT axial flux",
                 ha="center", fontsize=8, style="italic")
        pdf.savefig(fig, dpi=150)
        plt.close(fig)

        # Page 2: unrolled + dims
        fig = plt.figure(figsize=(11, 8.5))
        fig.suptitle(TITLE, fontsize=11, fontweight="bold", y=0.98)
        ax1 = fig.add_axes([0.05, 0.48, 0.90, 0.42])
        fig_unrolled(fig, ax1)
        ax2 = fig.add_axes([0.08, 0.05, 0.40, 0.38])
        fig_dims_table(fig, ax2)
        ax3 = fig.add_axes([0.52, 0.05, 0.45, 0.38])
        fig_conflict(fig, ax3)
        pdf.savefig(fig, dpi=150)
        plt.close(fig)

        # Page 3: BOM
        fig = plt.figure(figsize=(11, 8.5))
        fig.suptitle(TITLE, fontsize=11, fontweight="bold", y=0.98)
        ax = fig.add_axes([0.08, 0.08, 0.84, 0.82])
        fig_bom_table(fig, ax)
        pdf.savefig(fig, dpi=150)
        plt.close(fig)

    # PNG preview = page-1 style composite
    fig = plt.figure(figsize=(11, 8.5))
    fig.suptitle(TITLE, fontsize=11, fontweight="bold", y=0.98)
    ax1 = fig.add_axes([0.05, 0.08, 0.55, 0.82])
    fig_axial_section(fig, ax1)
    ax2 = fig.add_axes([0.58, 0.35, 0.40, 0.55])
    fig_rotor_polar(fig, ax2)
    fig.text(0.72, 0.12, "Austin Carolino  ·  units mm  ·  preview",
             ha="center", fontsize=8, style="italic")
    fig.savefig(png_path, dpi=150)
    plt.close(fig)

    # SVG too
    svg_path = OUT / "HF-RF16-DRAWING.svg"
    fig = plt.figure(figsize=(11, 8.5))
    fig.suptitle(TITLE, fontsize=11, fontweight="bold", y=0.98)
    ax1 = fig.add_axes([0.05, 0.08, 0.55, 0.82])
    fig_axial_section(fig, ax1)
    ax2 = fig.add_axes([0.58, 0.35, 0.40, 0.55])
    fig_rotor_polar(fig, ax2)
    fig.savefig(svg_path, format="svg")
    plt.close(fig)

    print(f"Wrote {pdf_path}")
    print(f"Wrote {png_path}")
    print(f"Wrote {svg_path}")


if __name__ == "__main__":
    main()
