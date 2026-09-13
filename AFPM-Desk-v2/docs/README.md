# Generator Experiments v2 — AFPM-Desk Dual-Rotor Sandwich

**Owner:** Austin Carolino  
**Build name:** AFPM-Desk-v2  
**Purpose:** Desktop educational **dual-rotor axial-flux permanent-magnet (AFPM)** generator with **steel back-iron**.  
**Not a free-energy / overunity device.** Electrical energy out ≤ mechanical energy in (hand crank). Orthodoxy: Maxwell–Faraday induction + energy conservation only.

**Date package:** 2026-09-10 (America/New_York)  
**Evolves from:** v1 AFPM-Desk (single rotor, 8× N42, 6 coils) — Drive folder [v1](https://drive.google.com/drive/folders/12ztOcHBTHuGbHydsOmjWQckuVxojFjWz)

---

## What changed vs v1

| Feature | v1 | v2 (this package) |
|---------|----|-------------------|
| Topology | Single rotor / single stator | **SSDR sandwich**: dual rotors + stator between |
| Magnets | 8× N42 Ø20×3 | **8+8** (16×) N42 Ø20×3 facing across stator |
| Back-iron | None (plastic return) | **Mild steel discs** Ø100×1.5 mm behind each magnet set |
| Coils | 6 | **6** (continuity; 3-phase capable) |
| Expected B_g | ~0.25–0.40 T | ~**0.40–0.60 T** (order-of-magnitude) |
| Air gap | 2–3 mm one side | **1.5–2.5 mm each side** magnet↔coil |
| Learning goal | Basic Faraday demo | Higher flux, feel stronger cogging, compare single vs dual |

---

## Package contents

| Path | Description |
|------|-------------|
| `README.md` | This overview |
| `BUILD.md` | Assembly steps + print notes |
| `PARTS.md` | Labeled part list, BOM, physics debrief per part |
| `SCHEMATIC.md` | Polarity, wiring, mechanical stack |
| `PHYSICS.md` | Faraday estimates, citations, sanity checks |
| `FIT_COUPON.md` | Print-first clearance coupon procedure |
| `PRINT_NOTES.md` | Orientation, supports, pause-for-magnets |
| `scad/*.scad` | Parametric OpenSCAD sources |
| `stl/*.stl` | Binary STLs for Anycubic Kobra 3 Max |

---

## Topology choice (documented)

**8+8 magnets / 6 coils** kept deliberately:

1. **Continuity with v1** — reuse coil winding skill and 8-magnet pattern; buy 8 more discs.
2. **Educational clarity** — alternating N/S on each rotor; facing magnets **attract** (N faces S across gap) so flux threads the coils axially.
3. **3-phase option** — wire coils as A=(C0+C3), B=(C1+C4), C=(C2+C5) like v1.
4. **Why not 12/9 yet?** Commercial DIY AFPM often uses 12 poles / 9 coils for smoother 3-phase at wind-turbine scale (Latoufis et al.). For desk hand-crank learning, 8/6 is adequate and simpler. A v3 could migrate to 12+12/9 if wanted.

**Steel back-iron role:** provides a low-reluctance return path between adjacent poles on each rotor, raising air-gap flux density versus the plastic-only v1 disc, and reducing stray flux behind the magnets (Gieras / AFPM literature; Latoufis rural-electrification AFPM notes).

**Coreless stator:** plastic plate + copper coils only — **no iron teeth** → low cogging for hand crank (still some detent from magnet–magnet attraction across the gap). Tradeoff: thicker magnetic gap than slotted iron stator → B_g lower than industrial iron-cored AFPM, but safer and smoother for learning.

---

## Quick start

1. Print **`fit_coupon.stl` first** → measure → tweak `scad/parameters.scad` if needed → re-export.
2. Read **PHYSICS.md** + **PARTS.md** (safety: neo pinch / eyes).
3. Print remaining STLs (PLA or PETG, 0.2 mm layers, ≥3–4 perimeters on rotors/frame).
4. Buy BOM (16× N42, 2× steel discs, 28 AWG, 608 bearings, Ø8 shaft ~220 mm).
5. Assemble per **BUILD.md**; set **~2 mm air gap each side**.
6. Measure open-circuit AC @ ~60–120 RPM; compare to PHYSICS estimates.

---

## Desk-scale electrical targets (order of magnitude)

- Hand crank **60–120 RPM** → roughly **~1–8 Vrms** open-circuit depending on series/3-phase wiring (see PHYSICS.md).
- Peak educational power: **order of watts** (LED / small loads), **not** mains / battery-bank charging without further engineering.
- Voltage stays **low-energy educational** at hand speed — still use eye protection for magnets.

---

## Physics stance (explicit)

Converts **mechanical → electrical**. Friction, I²R, and magnetic drag ⇒ η < 1. **No perpetual motion, free energy, or overunity claims.** Dual rotors and steel raise coupling; they do not create energy.

---

## Printer assumptions

Anycubic **Kobra 3 Max**, **0.4 mm nozzle**, **0.2 mm layers**, **PLA or PETG**. Skill: `/home/box/agent-data/workflows/kobra-stl-from-description/SKILL.md`.

---

## Upload note

Large binary STLs often cannot upload intact via the Google Drive connector. Docs (markdown) upload fine; place STLs in Drive **Generator Experiments / v2** manually from this package if needed.

Local root: `/workspace/generator-experiments/v2/`

---
*Generator Experiments · Magneat-o cycle · v2*
