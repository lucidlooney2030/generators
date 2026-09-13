# HF-RF16-SERP  16P/16S

**Radial-flux OUTER-ROTOR generator · single-phase wave (serpentine) winding**  
For **Austin Carolino** · units **mm** · FROM SCRATCH (not axial flux, no pancake coils, no 9-bobbin concentrated winding, no magnet platter).

| | |
|---|---|
| Topology | Rotor cup spins **around** stationary stator drum |
| Poles / slots | **16** disc magnets / **16** axial grooves |
| Winding | One continuous serpentine/wave, 26 AWG, target 80–120 turns |
| Air gap | **1.00 mm** (locked; do not exceed 1.2) |

---

## Geometry conflict resolution

**Problem.** Early notes mixed a drum bore of 47.00 with groove floor **r = 47.38**, leaving only **0.38 mm** of printed wall (below the ≥2.00 mm minimum). Sleeve outer was corrected to **r = 55.38** (wall 0.80), and a copper fill of “~7.2” no longer matched.

**Chosen resolution (preferred):**

| Stack item | Value |
|---|---|
| Magnet inner-face pitch radius | **56.38** |
| Air gap | **1.00** |
| Sleeve OUTER / INNER r | **55.38** / **54.58** (wall 0.80) |
| Printed bore **radius** | **47.00** → bore **Ø94.00** |
| Groove floor r | **49.00** (not 47.38) |
| Printed wall (bore → floor) | **2.00** |
| Copper radial fill | 55.38 − 0.80 − 49.00 = **5.58** (revises “7.2”) |
| Groove open (pre-sleeve) | r = **55.38** |
| Land / groove arcs @ 55.38 | **9.75** / **12.00** (sum 21.75 = pitch arc; **no ±0.5 tweak**) |

**Steel tube:** Legacy BOM “OD~47” matched the **bore radius** figure. Corrected bought tube: **OD ≈ 94 mm**, wall ~3 mm, length ~28 mm — slip fit in Ø94 bore.

Angular pitch remains **16 × 22.50°**.

---

## Key dimensions

| Parameter | mm |
|---|---|
| Magnets | 16× Ø20.00×5.00 NdFeB, faces inward, N-S-N-S |
| Magnet backs | r = 61.38 |
| Rotor OD | 132.00 |
| Back-iron groove | r = 61.38–62.88 × axial 20.20; strip cut **386** |
| Stator axial (groove+galleries) | 32.00 |
| Pocket Ø / depth / lip ID | 20.30 / 5.20 / 18.40 (lip thk 0.80) |
| 608ZZ seats | Ø22.20 × 7.20 deep (×2: rotor + cap) |

---

## Deliverables

| File | Description |
|---|---|
| `hf_rf16_params.py` | Locked parameters (`MAG_COUNT=16`) |
| `hf_rf16_cad.py` | Parametric CadQuery → STEP + STL |
| `hf_rf16_drawing.py` | Drawing generator |
| `HF-RF16-ROTOR.stl` / `.step` | Outer rotor cup |
| `HF-RF16-STATOR.stl` / `.step` | Grooved stator drum |
| `HF-RF16-SLEEVE.stl` / `.step` | Two 180° post-wind shells |
| `HF-RF16-CAP.stl` / `.step` | End cap + 2nd bearing |
| `HF-RF16-ASSEMBLY.step` | Positioned assembly |
| `HF-RF16-ONEPLATE.stl` | All parts, 8 mm gaps (300 mm bed) |
| `HF-RF16-DRAWING.pdf` (+ png/svg) | Dimensioned drawing set |
| `PHYSICS_NOTE.md` | Faraday sanity |
| `PRINT_NOTES.md` | Print orientation & settings |
| `BOM.md` | Bought + printed BOM |

Rebuild:

```bash
cd /workspace/generator-experiments/HF-RF16
.venv/bin/python hf_rf16_cad.py
.venv/bin/python hf_rf16_drawing.py
```

---

## Build overview

Print rotor (pockets up), stator (grooves up), sleeve halves (flat), and cap (flat) in PETG/ABS/ASA/nylon — never PLA. Press 16× Ø20×5 NdFeB into rotor pockets alternating N-S (centrifugal seats outboard; lip retains inward). Slide 1.5×20 mild-steel strip (cut 386) into the back-iron groove. Fit steel tube Ø94 into stator bore. Wave-wind 26 AWG through all 16 grooves with end-turn galleries (up 1, over, down 2, …), use the return slot for multi-turn, exit tails through cap grommets. Clip on sleeve halves after winding. Assemble on Ø8 shaft with two 608ZZ (rotor cup rotates; stator fixed via cap). Rectify with a 4-diode bridge and ≥1000 µF.

**Constraints honored:** radial flux only · magnets on inner wall of rotating cup · coil active length axial · serpentine pitch = pole pitch · no stator teeth · air gap 1.00.
