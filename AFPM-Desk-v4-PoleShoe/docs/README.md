# Generator Experiments v4 — AFPM-Desk-v4 PoleShoe

**Owner:** Austin Carolino  
**Build name:** AFPM-Desk-v4 PoleShoe  
**Purpose:** Desktop educational **SSDR dual-rotor axial-flux PM** generator with **mild-steel back-iron** plus **mild-steel pole shoes / flux concentrators** under each magnet.  
**Not a free-energy / overunity device.** Electrical energy out ≤ mechanical energy in (hand crank). Orthodoxy: Faraday induction + energy conservation only.

**Date package:** 2026-09-13 (America/New_York)  
**Evolves from:** v2 AFPM-Desk dual-rotor sandwich (`/workspace/generator-experiments/v2/`)

---

## What changed vs v2

| Feature | v2 | v4 (this package) |
|---------|----|-------------------|
| Topology | SSDR sandwich + steel back-iron | SSDR + **back-iron + pole shoes** |
| Magnets | 8+8 Ø20×**3** N42 | **12+12** Ø20×**5** N42 (Austin stock) |
| Flux teaching | Back-iron return path | Back-iron **+** Ø18×2 mm shoes under each magnet (reluctance / concentration) |
| Coils | 6 | **9** (true 3-phase Y or Δ) |
| Air gap | ~2 mm/side | **1.5–2.0 mm**/side (parametric spacers) |
| Material | PLA/PETG | **PETG** preferred (Kobra 3 Max) |
| Poles | P=8 → f=4·RPM/60 | **P=12 → f=6·RPM/60** |

---

## Package contents

| Path | Description |
|------|-------------|
| `README.md` | This overview |
| `BUILD.md` | Assembly steps + safety |
| `PARTS.md` | Labeled part list + debrief |
| `SCHEMATIC.md` | Polarity, wiring, mechanical stack |
| `PHYSICS.md` | Faraday estimates, citations, Voc OOM |
| `PRINT_NOTES.md` | Orientation, supports, PETG settings |
| `FIT_COUPON.md` | Print-first clearance coupon |
| `MANIFEST.md` | File inventory |
| `scad/*.scad` | Parametric OpenSCAD |
| `stl/*.stl` | Binary STLs |
| `sim/` | Numpy Voc vs RPM sanity check |

---

## Topology (why 12/9)

Classic low-speed AFPM educational choice (Latoufis et al. rural AFPM lineage):

1. **12 poles / 9 coils** → natural 3-phase with 120° electrical spacing of coil groups.
2. Thicker Ø20×5 magnets raise source MMF vs v2’s Ø20×3.
3. **Pole shoes** (mild steel, slightly smaller than magnet face) teach flux concentration and reluctance — shoes sit under each magnet, ahead of the full back-iron disc.
4. Coreless plastic stator keeps cogging hand-crankable (still strong dual-N42 attraction — **pinch hazard**).

---

## Quick start

1. Print **`stl/fit_coupon.stl` first** → measure → tweak `scad/parameters.scad` → re-export if needed.
2. Read **PHYSICS.md** + **PARTS.md** (neo pinch / eyes / steel tools).
3. Print remaining STLs (**PETG**, 0.2 mm layers, 5 perimeters / 40% infill / 100% around pockets).
4. Buy BOM: 24× N42 Ø20×5, 24× mild-steel Ø18×2 pole shoes, 2× mild-steel Ø118×1.5 back-iron discs, 28 AWG, 2× 608ZZ, Ø8 shaft ~250 mm.
5. Assemble per **BUILD.md**; set **~1.5–2.0 mm** air gap each side with spacer rings.
6. Measure Voc @ 60–180 RPM; compare to PHYSICS / `sim/`.

---

## Desk-scale electrical targets (order of magnitude)

- Hand crank **60–120 RPM** → roughly **~1–8 Vrms** open-circuit depending on series / Y wiring (see PHYSICS.md).
- @ **120 RPM** conservative model: ~**0.8–1.2 Vrms / coil**, ~**2.5–4 Vrms / phase** (3 coils series), LED-scale after Schottky bridge.
- Educational power: **order of watts**, not utility / battery-bank without further engineering.

---

## Physics stance (explicit)

Converts **mechanical → electrical**. Friction, I²R, eddy/hysteresis in steel, and magnetic drag ⇒ η < 1.  
**No perpetual motion, free energy, or overunity claims.** Pole shoes and thicker magnets improve **coupling** of the work you put in.

---

## Printer assumptions

Anycubic **Kobra 3 Max**, **0.4 mm nozzle**, **0.2 mm layers**, **PETG**.  
Skill: `/home/box/agent-data/workflows/kobra-stl-from-description/SKILL.md`.

Local root: `/workspace/generator-experiments/v4/`

---
*Generator Experiments · Magneat-o cycle · v4 PoleShoe*
