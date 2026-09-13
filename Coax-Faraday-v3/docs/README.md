# Generator Experiments v3 — Coaxial Faraday Desk Generator

**Austin Carolino** · educational Faraday machine · orthodox physics only  
**Not** free energy / overunity / perpetual motion.

## What it is
A **simple three-layer coaxial** hand-crank generator for Anycubic **Kobra 3 Max** (PETG, 0.4 mm nozzle, 0.2 mm layers):

1. **Outer** magnet drum — Ø20×5 mm N42 discs, faces **inward**
2. **Middle** fixed copper coil stator (bobbin)
3. **Inner** magnet drum — Ø20×5 mm N42 discs, faces **outward**

**Topology:** outer + inner drums are **mechanically locked** and rotate together as one rotor; the coil cylinder is the **stationary stator**. No brushes. Flux crosses the coil **radially**.

## Why this topology
- Stationary coils → no brushes, desk-safe low voltage
- Dual facing magnets raise gap flux vs single-sided
- Matched pole count (P=8) with alternating N/S around the circumference

## Magnet decision
**Assumption:** “20×5 mm” = **Ø20×5 mm discs** (not bar stock) — common catalog size (e.g. supermagnete S-20-05-N N42).

**Inner choice: Ø20×5 discs (not Ø3×5 cans).**  
Simulation FoM \(P\cdot\Phi\): Ø20 dual ≫ Ø3 dual (area ratio \((3/20)^2\approx2.25\%\)). Outer Ø20 already limits pole count, so tiny inner magnets buy no useful frequency and lose flux.

## Expected order of magnitude (@ 120 RPM, baseline)
From `sim/` (N42, P=8, 2 mm gaps, 26 AWG, dual Ø20):

| Quantity | Estimate |
|----------|----------|
| \(f\) | 8 Hz |
| Voc rms | **~4 V** |
| Voc peak | **~6 V** |
| LED current (100 Ω + 2 V LED, naive bridge) | **~17 mA** |

Hand-crank 60–300 RPM → LED demo territory; not a power plant.

## Package layout
```
v3/
  README.md  PHYSICS.md  DEBRIEF.md  SCHEMATIC.md  PRINT_NOTES.md
  scad/   parametric OpenSCAD
  stl/    binary STLs
  sim/    numpy sweep + CSV + plots
  scripts/export_stls.sh
```

## Quick start
1. Print `fit_coupon.stl` in PETG; dial magnet/bearing fits.
2. Print drums, stator halves, base, hubs, crank.
3. Epoxy magnets with **polarity_jig** (alternating).
4. Wind stator (26–28 AWG), assemble, crank into an LED + series resistor.

See **DEBRIEF.md** for BOM/assembly and **PHYSICS.md** for equations & safety.
