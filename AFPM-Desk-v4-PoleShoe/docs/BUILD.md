# BUILD — AFPM-Desk-v4 PoleShoe

## Safety first (read before touching magnets)

- **24× N42 Ø20×5** in dual arrays produce **violent snap / crush / pinch** forces. Keep fingers clear of the gap.
- Assemble rotors **one at a time**, magnets **epoxied** before bringing rotors near each other.
- Use **non-magnetic** tools (brass, plastic, wood). Keep steel screwdrivers / wrenches **away** from open magnet faces.
- Eye protection: NdFeB is brittle and can shatter.
- Children / pets: choke + pinch hazard. No mains connection in this design.

---

## 0. Fit coupon (mandatory first print)

Print `stl/fit_coupon.stl` in PETG. Measure shaft holes, 608ZZ seats, magnet Ø20×5 pocket, pole-shoe Ø18×2 pocket. Adjust `scad/parameters.scad` (`clearance_slip`, `press_interference`, `magnet_pocket_xy`, …) and re-export if needed. See `FIT_COUPON.md`.

---

## 1. Print list (PETG)

| Qty | STL | Notes |
|-----|-----|-------|
| 1 | `base_frame.stl` | Flat on bed |
| 1 | `rotor_disc_A.stl` | Flat; pause for magnets optional |
| 1 | `rotor_disc_B.stl` | Flat; polarity opposite etch |
| 1 | `stator_plate.stl` | Flat |
| 9 | `coil_bobbin.stl` | Wind then insert |
| 2 | `shaft_hub.stl` | |
| 2 | `bearing_cap.stl` | |
| 1 | `hand_crank.stl` | |
| 1 | `crank_handle.stl` | |
| 2+ each | `spacer_1mm/1p5mm/2mm.stl` | Air-gap tuning |
| 1 | `polarity_jig.stl` | Magnet install aid |
| 1 | `pole_shoe_holder.stl` | Optional teaching / dry-fit |
| 1 | `fit_coupon.stl` | First |
| 1 | `electronics_tray.stl` | Optional |

Settings: **5 perimeters**, **40% infill**, **100% infill around magnet/bearing pockets**, 0.2 mm layers. Details in `PRINT_NOTES.md`.

---

## 2. Wind coils

1. Wind each bobbin **~180–220 turns of 28 AWG** (or ~150 turns 26 AWG for lower R / higher current).
2. Leave 150 mm leads; tape; lightly varnish or hot-glue ends.
3. Label coils **0…8** around the stator (phase map in `SCHEMATIC.md`).
4. Drop bobbins into stator pockets; route leads through exit channels.

---

## 3. Rotor A / B magnet + shoe install

Stack per rotor (from back → front / stator face):

```
[printed rotor] ← steel back-iron disc in back recess
               ← Ø18×2 pole shoe in each under-pocket
               ← Ø20×5 N42 in magnet pocket (face toward stator)
```

1. Place **back-iron** in rear recess; retain with 3× M3 (non-magnetic fasteners preferred) or epoxy.
2. Drop **pole shoes** into under-pockets (epoxy).
3. Using `polarity_jig.stl`, install magnets **alternating N/S** per etch:
   - **Rotor A:** even stations N toward stator.
   - **Rotor B:** polarity chosen so **N faces S** across the gap at each angular station.
4. Epoxy magnets flush; wipe squeeze-out so face is flat (air-gap critical).
5. Do **not** bring completed rotors together until shaft + spacers are ready.

---

## 4. Frame & shaft

1. Press **608ZZ** into both base posts (coupon-verified seat). Cap with `bearing_cap`.
2. Slide Ø8 shaft through both bearings.
3. Mount **hub + rotor A** on one side; **hub + rotor B** on the other; use spacer rings to set **~1.5–2.0 mm** magnet-face ↔ coil-face each side.
4. Bolt stator to three pillars with M4; verify concentric clearance to shaft.
5. Attach crank + handle; M3 set screws on hubs and crank.

---

## 5. Electrical bring-up

1. Confirm free rotation by hand **before** closing to minimum gap — feel cogging increase as gap shrinks.
2. DMM ACV on one coil while cranking ~60–120 RPM.
3. Wire 3-phase Y or Δ per `SCHEMATIC.md`; Schottky bridge → LED + series resistor on tray.
4. Expect **Lenz drag** when LED loads — that is Faraday working, not a fault.

---

## 6. Acceptance checks

- [ ] Fit coupon measurements logged
- [ ] Magnets flush; no scrape at 1.5 mm gap
- [ ] Voc scales ≈ linearly with RPM
- [ ] Scope / DMM frequency ≈ `6 × RPM/60` (P=12)
- [ ] LED lights under vigorous hand crank (wiring-dependent)

---
*End BUILD*
