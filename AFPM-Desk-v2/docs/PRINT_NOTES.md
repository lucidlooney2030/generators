# PRINT_NOTES — Kobra 3 Max (AFPM-Desk-v2)

**Assumptions:** 0.4 mm nozzle, 0.2 mm layers, PLA or PETG, binary STLs.  
Skill reference: kobra-stl-from-description.

---

## Global settings

| Setting | Recommendation |
|---------|----------------|
| Layer height | 0.20 mm |
| Line width | 0.42–0.45 mm |
| Perimeters | **3–4** (rotors, base, hubs); 2–3 (spacers/jigs) |
| Infill | 25–40% gyroid/grid for rotors & base; 15% jigs |
| Top/bottom | ≥5 layers |
| Material | PETG preferred for RA/RB/BF; PLA OK elsewhere |
| Bed | Clean; brim 3–5 mm on tall posts if adhesion worries |
| Cooling | PLA normal; PETG moderate |

Bed envelope: parts fit Kobra 3 Max with ≫5 mm margin (largest ~180×160 mm base).

---

## Per-part orientation & supports

| Part | Orientation | Supports | Notes |
|------|-------------|----------|-------|
| fit_coupon | Flat as modeled | None | Print first |
| rotor_disc_A/B | **Back (steel recess) on bed** | None | Magnet pockets open upward; pause optional |
| stator_plate | Flat | None | Coil pockets up |
| base_frame | Flat base on bed | **Tree/supports under overhangs of posts if needed**; posts are vertical OK | Brim recommended |
| shaft_hub | Flange on bed | None | Bore axis vertical (roundness) |
| coil_former | Flat | None | |
| coil_bobbin | Flat | None | Print 6 |
| hand_crank | Flat | None | |
| crank_handle | Standing (axis Z) | None | |
| bearing_cap | Flat flange | None | Print 2 |
| spacer_* | Flat | None | Print extras |
| magnet_polarity_jig | Flat | None | |
| electronics_tray | Flat floor | None | |
| stator_clamp | Flat | None | Print 3–6 |

Overhangs designed ≤~45°. No long bridges >50 mm on critical faces.

---

## Pause for magnets (optional)

For **rotor_disc_A/B**:

1. Slice; note layer when magnet pocket floor is complete but before top solid layers close the pocket (pockets are open-top in this design — **pause not required** for open pockets).
2. If you modify to enclosed magnet capture lids: pause, insert magnets with correct polarity, resume.  
   **As shipped:** magnets epoxy in from the open face after printing — simpler and safer for first build.

Steel is installed **after** print into back recess — no pause needed.

---

## Clearances (designed)

| Feature | Designed fit |
|---------|----------------|
| Shaft in hub/crank | +0.35 mm slip |
| Bearing seat | ~0.15 mm undersize on OD (coupon!) |
| Magnet pocket XY | +0.25 mm on Ø |
| Magnet pocket depth | +0.15 mm |
| M3 clearance | 3.4 mm |
| M4 clearance | 4.3 mm |

**Always validate with fit_coupon** before committing filament to base/rotors.

---

## Post-processing

- Deburr magnet pocket rims lightly so discs seat flat.  
- Check bearing seats with 608 before final press.  
- Tap M3 set-screw holes carefully or use heat-set inserts (preferred for reuse).

---
*End PRINT_NOTES*
