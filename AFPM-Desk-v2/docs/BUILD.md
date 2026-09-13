# BUILD — AFPM-Desk-v2 Assembly Instructions

Read **PARTS.md** (safety) and **FIT_COUPON.md** before full prints.

---

## 0. Print-first coupon

1. Print `stl/fit_coupon.stl` (PLA, 0.2 mm, 3 perimeters).
2. Test-fit Ø8 shaft, 608 bearing, N42 disc, M3 screw.
3. Adjust `scad/parameters.scad` (`clearance_slip`, `press_interference`, `magnet_pocket_xy`) if needed.
4. Re-export affected STLs with OpenSCAD.

---

## 1. Print all parts

See **PRINT_NOTES.md** for orientation / supports / pause layers.

**Minimum set:**
- 1× fit_coupon (done)
- 1× rotor_disc_A, 1× rotor_disc_B
- 1× stator_plate
- 1× base_frame
- 2× shaft_hub
- 1× coil_former (+ optional 6× coil_bobbin)
- 1× hand_crank, 1× crank_handle
- 2× bearing_cap
- spacers: several 1.0 / 1.5 / 2.0 mm
- 1× magnet_polarity_jig
- 1× electronics_tray
- 3–6× stator_clamp

Suggested filament: **PETG** for rotors/base (toughness); PLA OK for jigs/spacers.

---

## 2. Prepare purchased bits

1. Cut Ø8 shaft ~220 mm; deburr ends.
2. Drill/cut center hole Ø14 mm in each steel disc if not pre-cut; deburr.
3. Mark N/S on all 16 magnets with a reference magnet + permanent marker.

---

## 3. Magnet + steel install (critical)

**Rotor A (etch pattern = even N facing stator):**

1. Place disc **magnet-pocket face UP**.
2. Using jig (rotor-A pattern): epoxy magnets into pockets, alternating N/S per etch on back.
3. Cure fully (hours).
4. Flip; epoxy **steel disc into back recess**; optional M3 screws through steel into plastic (short screws — don’t pierce magnet pockets).
5. Magnets must face **away from steel** (toward stator in final stack).

**Rotor B:**

1. Same process but **invert polarity** vs A at each angular station (use B etch / opposite of jig).
2. When assembled face-to-face, each A magnet’s N should face a B magnet’s S.

**Warning:** After both rotors have magnets+steel, they **slam together** with high force. Store separated by thick wood/foam; never leave facing freely.

---

## 4. Wind coils

1. Wind **6 coils**, ~**200 turns** 28 AWG on `coil_former` (or on `coil_bobbin`).
2. Same wind direction for all; mark **start** (dot) and **finish**.
3. Leave 15 cm leads; tape; remove former (kerf).
4. Sand enamel; tin leads.
5. Measure R ≈ 3–5 Ω each; discard opens/shorts.

---

## 5. Frame + bearings

1. Press 608 bearings into base_frame posts (coupon-verified fit).
2. Install bearing_caps loosely.
3. Slide shaft through both bearings; check spin.

---

## 6. Mount rotors on shaft

Suggested axial order (crank end = −Y):

```
CRANK | BRG | H1+RA(+steel out) | air | STATOR | air | RB(+steel out)+H2 | BRG
```

1. Bolt hub H1 to rotor A (M3×12); set-screw hub to shaft near crank bearing.
2. Magnets of A face **+Y** (toward center).
3. Mount stator on three M4 pillars with clamps; leave loose for gap set.
4. Bolt hub H2 to rotor B; magnets face **−Y** (toward center).
5. Bring B toward stator **slowly with spacers** already estimating 2 mm/side — do not pinch fingers.
6. Set-screw H2; verify angular alignment: N on A opposite S on B (mark matching index).

---

## 7. Set air gaps

1. Use feeler gauge or stacked `spacer_*` rings between magnet face and coil face.
2. Target **1.5–2.5 mm each side** (start **2.0 mm**).
3. Equalize both sides so stator is centered.
4. Spin by hand: **no scrape**, mild cogging OK.
5. Tighten stator clamps / pillar nuts.

---

## 8. Wire + electronics

1. Seat coils in stator pockets (or bobbins); hot-glue lightly.
2. Route leads via wire channels to electronics_tray.
3. First wiring: see **SCHEMATIC.md** — start with one phase (2 coils series) → bridge → LED+resistor.
4. Confirm series **aiding** (voltage increases when pair connected).

---

## 9. First light / measurements

1. Multimeter **ACV** on coil pair while cranking ~60–120 RPM.
2. Compare to PHYSICS.md (~1–2 Vrms per phase ballpark @ 120 RPM).
3. Connect rectifier + LED; note crank drag increase (Lenz).
4. Log RPM, Voc, Vdc, gap.

---

## 10. Failure quick-ref

| Symptom | Fix |
|---------|-----|
| Tiny V | Gap too large; wrong polarity facing; enamel not stripped |
| Rotor won’t turn | Gap too small; rotors slamming — add spacers |
| Scrape | Warped stator/rotor; re-level; increase gap |
| Phase cancel | Reverse one coil in series pair |
| Magnet exit | Re-epoxy; ensure pocket depth full |

---
*End BUILD — AFPM-Desk-v2*
