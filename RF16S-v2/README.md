# RF16S-v2 — dual-rotor radial flux (CURRENT)

**This is newer than everything else in this repo from 2026-09-13.**

Do not print AFPM-Desk-v1, AFPM-Desk-v2, HF-RF16, or HF-RF88 for this build. Those are earlier machines. This folder is the water-turbine radial generator:

- 16 × Ø20×5 mm discs on the **outer** cup, facing in
- 48 × Ø5×5 mm N52 cylinders on the **inner** hub (16 poles × 3 stacked), facing out
- 16-window coil cage between them
- Matched 16/16 poles, 22.5° pitch, 1.00 mm air gap both sides

## Print these four STLs

| File | What it is |
|---|---|
| `stl/HF-RF16S-v2-OUTER.stl` | Outer cup |
| `stl/HF-RF16S-v2-INNER.stl` | Inner hub (rim + spokes, not a solid puck) |
| `stl/HF-RF16S-v2-CAGE.stl` | Coil cage |
| `stl/HF-RF16S-v2-CAP.stl` | End cap |

Direct downloads (once the STLs are in this folder):
- https://github.com/lucidlooney2030/generators/raw/main/RF16S-v2/stl/HF-RF16S-v2-OUTER.stl
- https://github.com/lucidlooney2030/generators/raw/main/RF16S-v2/stl/HF-RF16S-v2-INNER.stl
- https://github.com/lucidlooney2030/generators/raw/main/RF16S-v2/stl/HF-RF16S-v2-CAGE.stl
- https://github.com/lucidlooney2030/generators/raw/main/RF16S-v2/stl/HF-RF16S-v2-CAP.stl

## Anycubic / Orca

- PETG. Not PLA.
- **Supports = Off**
- Slicer brim = Off (a 0.6 mm brim is already on the part)
- Layer 0.20 mm, first layer 0.24 mm
- 4 walls, 20% gyroid
- Outer walls first
- First layer 20 mm/s, bed ~75 °C, nozzle ~240 °C
- Pockets and cage windows face **up**
- Peel the brim when cold

## Magnets

Outer: N-S-N-S around the circle.
Inner: each column of 3 small magnets is one pole, all three the same way, **opposite** the outer magnet it faces (they attract across a window).

Steel strip 1.5 × 20 mm behind **both** rings.
