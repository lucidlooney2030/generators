# Serpentine PM Generator v1

Dual-magnet radial generator. 16 outer N52 Ø20×5 mm discs + 48 inner N52 ×5×5 mm discs (groups of 3). Serpentine coil former with through-holes for weaving.

## Files
- `01_outer_magnet_rotor.stl` — 16 pockets, Ø20.40 × 5.35 mm
- `02_inner_magnet_hub.stl` — 16 groups × 3, ×5.40 × 5.35 mm
- `03_serpentine_coil_former.stl` — 32 columns × 5 rows, Ø2.5 mm through-holes
- `04_stator_cap_stand.stl` — 608 bearing pocket + 3 legs
- `serpentine_pm_generator.scad` — OpenSCAD source (edit params, re-render)
- `serpentine_pm_generator.py` — CadQuery source (preferred for simulation)

## Winding
Wave all 16 even columns (outer), then all 16 odd columns (inner), same direction. Do not zigzag — that cancels 16 poles. Stack ~8 passes AWG 22.

## Process
This is the baseline for the parametric pipeline. Next changes go through `parameters.py` → regenerate → simulate → commit. See companion repos: parametric-cad-pipeline, cad-process-docs.
