# FIT_COUPON — Print Before the Generator

File: `stl/fit_coupon.stl` · Source: `scad/fit_coupon.scad`

## Why

FDM holes shrink; bearing press fits are printer-specific. One 80×50×6 mm coupon saves wasted rotors.

## What’s on the coupon

1. **Shaft hole ladder** — Ø8.2, 8.3, 8.4, 8.5 mm (approx.)  
2. **Bearing pocket variants** — three 608 OD seats with slight interference steps  
3. **Magnet pocket** — Ø20.25 × depth ~3.15 mm  
4. **M3 clearance + tap pilot**

## Procedure

1. Print in the **same material/profile** you’ll use for rotors (PETG recommended).  
2. Test Ø8 rod: choose slip that spins freely without slop → set `clearance_slip` in `parameters.scad`.  
3. Press 608 into the pocket that holds firmly without cracking → set `press_interference` / `bearing_seat_od`.  
4. Drop N42 into magnet pocket: snug, flush or 0.1–0.2 mm proud OK → adjust `magnet_pocket_xy` / `magnet_pocket_z`.  
5. Re-render STLs if you changed parameters:

```bash
cd /workspace/generator-experiments/v2
openscad -o stl/rotor_disc_A.stl --export-format=binstl scad/rotor_disc_A.scad
# …repeat for affected parts
```

6. Only then print RA/RB/base_frame.

---
*End FIT_COUPON*
