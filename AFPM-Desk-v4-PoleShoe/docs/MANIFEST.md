# MANIFEST — AFPM-Desk-v4 PoleShoe

Package root: `/workspace/generator-experiments/v4/`  
Archive: `/workspace/afpm_desk_v4_full_package.tar.gz`

## Documentation

- README.md
- BUILD.md
- PARTS.md
- SCHEMATIC.md
- PHYSICS.md
- PRINT_NOTES.md
- FIT_COUPON.md
- MANIFEST.md (this file)

## OpenSCAD (`scad/`)

- parameters.scad
- rotor_disc.scad, rotor_disc_A.scad, rotor_disc_B.scad
- stator_plate.scad, coil_bobbin.scad
- base_frame.scad, shaft_hub.scad, bearing_cap.scad
- hand_crank.scad, crank_handle.scad
- spacer_ring.scad, spacer_1mm.scad, spacer_1p5mm.scad, spacer_2mm.scad
- fit_coupon.scad, polarity_jig.scad, pole_shoe_holder.scad
- electronics_tray.scad

## Binary STLs (`stl/`)

- base_frame.stl
- rotor_disc_A.stl, rotor_disc_B.stl
- stator_plate.stl, coil_bobbin.stl
- shaft_hub.stl, bearing_cap.stl
- hand_crank.stl, crank_handle.stl
- spacer_1mm.stl, spacer_1p5mm.stl, spacer_2mm.stl
- fit_coupon.stl, polarity_jig.stl, pole_shoe_holder.stl
- electronics_tray.stl

## Simulation (`sim/`)

- afpm_desk_v4.py
- sweep_results.csv
- sim_summary.txt
- voc_vs_rpm.png, voc_vs_gap.png

## Regenerating STLs

```bash
cd /workspace/generator-experiments/v4
for p in scad/*.scad; do
  b=$(basename "$p" .scad)
  case "$b" in parameters|rotor_disc|spacer_ring) continue;; esac
  openscad -o "stl/${b}.stl" "$p"
done
# then convert ASCII→binary if needed via trimesh / stl2bin
```
