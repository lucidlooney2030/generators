# PARTS — AFPM-Desk-v4 PoleShoe

Labeled BOM + short physics debrief per group. Orthodoxy only.

---

## Printed parts

| Label | Part | Qty | Key dims (mm) | Debrief |
|-------|------|-----|---------------|---------|
| P1 | `base_frame` | 1 | 200×180×8 base; posts Ø36×78; spacing 145 | Locates dual 608ZZ axis + stator pillars; desk-safe footprint |
| P2 | `rotor_disc_A` | 1 | Ø130×11; 12× magnet + shoe pockets; steel recess | Carries magnets/shoes/back-iron; polarity etch N/S |
| P3 | `rotor_disc_B` | 1 | same | Opposite etch so N faces S across stator |
| P4 | `stator_plate` | 1 | Ø140×12; 9 coil pockets @ PCD 90 | Coreless — copper only in gap (low cogging vs iron teeth) |
| P5 | `coil_bobbin` | 9 | core 24×16×9.2 + flanges | Defines turn length / fill; stays in stator |
| P6 | `shaft_hub` | 2 | flange Ø36; boss Ø11.8; collar | Couples Ø8 shaft ↔ rotor (M3 set + 4× M3) |
| P7 | `bearing_cap` | 2 | — | Retains 608ZZ |
| P8 | `hand_crank` | 1 | arm 90 | Mechanical input — the energy source |
| P9 | `crank_handle` | 1 | Ø14×45 | Ergonomics |
| P10 | `spacer_*` | 2+ each | Ø30×{1.0,1.5,2.0} | Sets air gap (reluctance lever) |
| P11 | `polarity_jig` | 1 | Ø126×4; 12 stations | Prevents polarity mistakes |
| P12 | `pole_shoe_holder` | 1 | optional | Teaching dry-fit of Ø18 shoes |
| P13 | `fit_coupon` | 1 | 95×55×8 | Clearance calibration |
| P14 | `electronics_tray` | 1 | 80×55×14 | Bridge + LED |

---

## Purchased hardware

| Label | Item | Qty | Spec | Notes |
|-------|------|-----|------|-------|
| M1 | N42 neodymium disc | **24** | **Ø20×5 mm**, axially magnetized | Austin stock; grade Br ~1.28–1.32 T |
| M2 | Mild-steel pole shoe | **24** | **Ø18×2 mm** disc / punched blank | Flux concentrator under each magnet |
| M3 | Mild-steel back-iron | **2** | **Ø118×1.5 mm**, ID ~16 mm | Return path between adjacent poles |
| B1 | Bearing | 2 | **608ZZ** / 608-2RS (Ø22×Ø8×7) | Dual support |
| S1 | Shaft | 1 | Ø8 mm × ~250 mm steel or stainless | Non-magnetic shaft optional but not required |
| W1 | Magnet wire | 1 spool | **28 AWG** enamel (26 AWG alt.) | ~200 turns/coil target |
| F1 | Fasteners | assorted | M3×8–16, M4×20–40, set screws | Prefer brass/SS near magnets |
| E1 | Epoxy | — | 5–30 min | Magnets + shoes |
| E2 | Schottky bridge + LED + resistor | 1 set | e.g. 1N5819×4, 5 mm LED, 100–220 Ω | Desk demo |
| C1 | Ø3×5 neo cans | optional | Austin stock | Not used in baseline v4 rotors; reserved for future / jig |

---

## Part-group physics notes

### Magnets (M1)
Source of **remanent flux**. Do not create energy — they set B in the magnetic circuit. Thicker than v2 (5 vs 3 mm) → higher source MMF for same gap.

### Pole shoes (M2)
Mild steel (µ_r ≫ 1) under each magnet **lowers local reluctance** and can **concentrate** flux toward the magnet face / gap. Shoes slightly undersize (Ø18 vs Ø20) keep a plastic wall and illustrate concentration geometry. They also add a bit of eddy/hysteresis loss at higher RPM — negligible at hand crank.

### Back-iron (M3)
Provides circumferential return between adjacent N/S poles on each rotor (classic AFPM). Raises useful air-gap flux vs plastic-only return (v1 lesson).

### Coils (P5 + W1)
Faraday sensors: \(\mathcal{E}=-N d\Phi/dt\). More turns → more V and more R. Nine coils enable clean 3-phase.

### Air-gap spacers (P10)
Primary experimental knob: larger gap → lower \(B_g\) → lower Voc (reluctance).

---

## Cost / sourcing ballpark

Neo discs and steel blanks dominate. Expect educational BOM on the order of tens of USD if magnets already owned (Austin has Ø20×5). Pole-shoe discs can be punched/laser-cut from 2 mm mild sheet or bought as Ø18×2 neodymium-free steel spacers.
