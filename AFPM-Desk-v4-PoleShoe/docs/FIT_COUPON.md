# FIT_COUPON — print first

File: `stl/fit_coupon.stl` (95×55×8 mm)

## What it tests

1. **Shaft hole ladder** — Ø8.2, 8.3, 8.4, 8.5 (pick slip fit for Ø8 shaft).
2. **608ZZ seats** — OD −0.20 / −0.15 / −0.10 mm (pick firm press).
3. **Magnet pocket** — Ø20.25 × depth ~5.15 for Ø20×5 disc.
4. **Pole-shoe pocket** — Ø18.30 × depth ~2.15 for Ø18×2 steel.
5. **M3 clear (3.4) / tap pilot (2.5)**.

## Procedure

1. Print in **PETG**, same settings as final parts.
2. Calipers: record actual hole IDs and pocket depths.
3. Edit `scad/parameters.scad`:
   - `clearance_slip`, `press_interference`
   - `magnet_pocket_xy`, `magnet_pocket_z`
   - `pole_shoe_pocket_xy`, `pole_shoe_pocket_z`
4. Re-export affected STLs with OpenSCAD before printing rotors/frame.

Do **not** skip this — dual neo arrays punish bad fits.
