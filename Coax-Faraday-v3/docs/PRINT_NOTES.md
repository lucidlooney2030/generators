# PRINT_NOTES — Kobra 3 Max (v3)

## Printer profile
- **Anycubic Kobra 3 Max**, 0.4 mm nozzle, **0.2 mm** layers  
- Material: **PETG preferred** (drums, base, hubs — toughness + temp)  
- PLA OK for fit_coupon / polarity_jig / spacers  
- Bed: PEI, dry filament; PETG bed ~70–85 °C, nozzle ~230–250 °C (tune to brand)  
- Walls: ≥4 perimeters on drums (**≥2 mm** wall param)  
- Infill: 25–40% gyroid/grid on structural; 15% OK on jig  
- Supports: generally **none** if oriented as below; tree supports only if needed under base post arches

## Orientation
| Part | On bed | Notes |
|------|--------|-------|
| fit_coupon | flat | as modeled |
| inner / outer drums | closed/flat end on bed | pockets face up/side; minimize support in pockets |
| stator_bobbin | flat feet down | halves already laid out |
| base | floor on bed | posts vertical |
| shaft_hub, end_cap, bearing_cap | flat face down | |
| hand_crank | arm flat on bed | |
| polarity_jig | flat | |

## Fit targets (from kobra skill)
- Magnet pocket: **Ø +0.2–0.3 mm**, depth **+0.1–0.2 mm** (params use +0.25 / +0.15)  
- 608 press: seat **~0.1–0.2 mm undersize on diameter** (`bearing_seat_od = 22 − 0.15`)  
- Always print **fit_coupon** first and adjust `parameters.scad` before committing drums

## Post-process
- Deburr pocket edges so magnets seat flat  
- Tap M3 set-screw holes or use heat-set inserts in hubs/crank  
- Light sand on stator split faces for a tight clamp

## Export
```bash
./scripts/export_stls.sh
```
OpenSCAD 2021.01+, binary STL, mm units.
