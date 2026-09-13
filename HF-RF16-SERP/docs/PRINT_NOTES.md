# PRINT_NOTES — HF-RF16-SERP

## Material

**PETG / ABS / ASA / nylon** — **NOT PLA** (creep, heat near magnets/bearings, poor fatigue).

## Settings (baseline)

| Setting | Value |
|---|---|
| Min wall | ≥2.00 mm |
| Perimeters | **5** |
| Infill | **40%** |
| Local solid | **100% infill within ~3 mm** of magnet pockets, grooves, bearing seats, bosses |
| Layer height | 0.20 mm (0.15 near bearing bores if possible) |
| Nozzle | 0.4 mm |

## Orientation

| Part | Orientation |
|---|---|
| Rotor | **Pockets UP** (magnet cavities open to +Z). Floor/boss on bed. Supports OK inside cup if needed for lips. |
| Stator | **Grooves UP** (open outward grooves face +Z / side per slicer — prefer drum axis vertical, grooves visible from top). |
| Sleeve halves | **Flat** on bed (OD or ID down — prefer OD down for clip accuracy). |
| Cap | **Flat** on bed (cover face down or boss up; prefer boss UP). |

## One-plate

`HF-RF16-ONEPLATE.stl` — parts spaced **8 mm**, fits a **300 mm** bed. Still print rotor alone if you want max quality on pockets.

## Post-print

- Ream 608ZZ seats to press-fit (bore printed 22.20 for 22.00 bearing).
- Stator M3 pilots are **Ø2.5** — for **heat-set M3 inserts** or tap M3×0.5.
- Rotor: 6× Ø3.20 clearance on 40 mm circle (turbine coupling).
- Deburr groove edges before winding; keep sleeve ID clear (54.58).
- Do **not** anneal PLA — you should not have used PLA.

## Fit checks before magnets

1. Sleeve halves close over wound stator to outer r≈55.38.
2. Rotor spins over sleeved stator with **~1.00 mm** radial clearance to magnet faces (feel with feeler / paper after dry-fit magnets carefully).
3. Shaft Ø8 through both 608ZZ; stator held by cap; rotor free.
