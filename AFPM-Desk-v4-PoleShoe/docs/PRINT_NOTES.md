# PRINT_NOTES — AFPM-Desk-v4 PoleShoe

**Printer:** Anycubic Kobra 3 Max  
**Nozzle:** 0.4 mm  
**Layer:** 0.2 mm  
**Material:** **PETG** (not PLA — better heat / toughness for magnet forces)

---

## Global settings

| Setting | Value |
|---------|-------|
| Perimeters | **5** |
| Infill | **40%** gyroid/grid |
| Around magnet / bearing / shoe pockets | **100%** solid (paint-on or modifier) |
| Top/bottom | ≥ 5 layers |
| Temps | PETG typical (hotend ~240 °C, bed ~80 °C — match your filament) |
| Cooling | moderate (PETG); avoid warping on large discs |
| Supports | generally **none** if printed as oriented below |

---

## Orientation

| Part | Orientation | Notes |
|------|-------------|-------|
| base_frame | Base flat on bed | Elephant-foot on posts OK |
| rotor_disc_A/B | Flat (back or front) | Roundness of pockets critical — Z axis = bore axis |
| stator_plate | Flat | Coil pocket floors down or up OK |
| coil_bobbin | Flange flat | ×9 |
| shaft_hub | Flange flat | Bore vertical |
| bearing_cap | Flat | |
| hand_crank | Flat | |
| crank_handle | Standing (axis Z) | |
| spacers | Flat | |
| fit_coupon | Flat | **print first** |
| polarity_jig | Flat | |
| pole_shoe_holder | Flat | optional |

---

## Pause / insert (optional)

Advanced: pause mid-rotor to drop pole shoes then magnets, then resume — only if you trust pause accuracy. **Default:** print complete, epoxy shoes then magnets after printing (safer).

---

## Post-process

- Deburr magnet / shoe pocket edges lightly.
- Check 608ZZ press: should be firm, not crush plastic.
- PETG can string — quick heat-gun / trim on shaft bores.

---

## Skill rules applied

From `kobra-stl-from-description/SKILL.md`: walls ≥ 0.8 mm (housings 2.0–2.5); magnet pocket Ø +0.25, depth +0.15; bearing seat ~0.15 undersize total; M3 clear 3.4; elephant-foot chamfer on rotor rim.
