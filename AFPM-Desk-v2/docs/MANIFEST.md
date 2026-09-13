# MANIFEST — Generator Experiments v2

**Build:** AFPM-Desk-v2 Dual-Rotor Sandwich  
**Created:** 2026-09-10 (America/New_York)  
**Root:** `/workspace/generator-experiments/v2/`

## Documentation

| File | Description |
|------|-------------|
| README.md | Overview, topology choice, quick start |
| BUILD.md | Assembly instructions |
| PARTS.md | Labeled parts, BOM, per-part debrief |
| SCHEMATIC.md | Polarity, wiring, stack diagrams |
| PHYSICS.md | Faraday estimates, citations, non-claims |
| PRINT_NOTES.md | Kobra 3 Max orientation / supports / pause |
| FIT_COUPON.md | Clearance coupon procedure |
| MANIFEST.md | This file |

## OpenSCAD (`scad/`)

parameters.scad, rotor_disc.scad, rotor_disc_A.scad, rotor_disc_B.scad, stator_plate.scad, base_frame.scad, shaft_hub.scad, coil_former.scad, coil_bobbin.scad, hand_crank.scad, crank_handle.scad, bearing_cap.scad, spacer_ring.scad, spacer_1mm.scad, spacer_1p5mm.scad, spacer_2mm.scad, magnet_polarity_jig.scad, electronics_tray.scad, stator_clamp.scad, fit_coupon.scad

## Binary STLs (`stl/`)

fit_coupon, rotor_disc_A, rotor_disc_B, stator_plate, base_frame, shaft_hub, coil_former, coil_bobbin, hand_crank, crank_handle, bearing_cap, spacer_1mm, spacer_1p5mm, spacer_2mm, magnet_polarity_jig, electronics_tray, stator_clamp

## Regenerate STLs

```bash
cd /workspace/generator-experiments/v2
bash scripts/export_stls.sh
```
