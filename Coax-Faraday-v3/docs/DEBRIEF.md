# DEBRIEF — Coax Faraday v3

## Labeled parts (print)

| STL | Role | Qty |
|-----|------|-----|
| `fit_coupon.stl` | Magnet + 608 fit calibration | 1 |
| `outer_magnet_drum.stl` | Outer rotor cup, Ø20×5 pockets (N-in / S-in alt.) | 1 |
| `inner_magnet_drum.stl` | Inner rotor, Ø20×5 pockets (N-out / S-out alt.) | 1 |
| `stator_bobbin.stl` | Split coil former (both halves in one STL) | 1 file |
| `shaft_hub.stl` | Locks outer closed end + pilots inner to shaft | 1 |
| `rotor_end_cap.stl` | Open-end lock: outer drum ↔ shaft | 1 |
| `base.stl` | Floor + two 608 posts | 1 |
| `bearing_cap.stl` | Bearing retainers | 2 |
| `hand_crank.stl` + `crank_handle.stl` | Drive | 1+1 |
| `polarity_jig.stl` | Alternating N/S seating guide | 1 |
| `spacer_*.stl` | Axial shims 1 / 1.5 / 2 mm | as needed |

**Bought hardware**

| Item | Spec | Qty | ~USD |
|------|------|-----|------|
| NdFeB discs | Ø20×5 mm N42 (Ni) | 16 | 25–40 |
| 608-2RS bearings | 8×22×7 mm | 2 | 3–6 |
| Shaft | Ø8 mm steel rod ~150 mm | 1 | 3–5 |
| Magnet wire | 26 AWG (or 28) enamel Cu ~30–50 m | 1 | 8–12 |
| M3 screws/nuts | assorted 8–20 mm | ~20 | 3–5 |
| Epoxy | 5–min or slow clear | 1 | 5–8 |
| LED + 100 Ω | demo load | 1 set | 1 |
| Bridge rectifier | W04G or 4×1N4007 | 1 | 1–2 |
| **Total** | | | **~50–80 USD** |

Optional: multimeter, hand tach / phone RPM app, thin wood stick for magnet placement.

---

## Assembly (short)

1. **Fit coupon** — confirm magnet press/slip and 608 seat; adjust OpenSCAD `magnet_pocket_xy` / `press_interference` if needed; reprint drums only if off.
2. **Magnets** — using `polarity_jig`, mark alternating poles. Epoxy 8 into **inner** (faces out) and 8 into **outer** (faces in). Match angles so facing pairs are N-in/N-out (see SCHEMATIC). Cure fully.
3. **Wind stator** — clamp bobbin halves; wind 26 AWG into the radial window (aim fill ~50–60%). Bring out leads through exit slot. Tape/varnish. Mount feet to base.
4. **Rotor** — press bearings into base posts; shaft through. Mount `shaft_hub` + outer drum closed end + inner drum on shaft so magnets align axially with coil. Fit `rotor_end_cap`. Verify **~2 mm** radial air gap each side (no rub).
5. **Crank** — attach hand crank; spin free (expect cogging).
6. **Electrical** — coil → bridge → 100 Ω → LED (or Voc on DMM AC/DC as wired).

---

## What to measure

| Test | Method | Expect (order) |
|------|--------|----------------|
| Voc vs RPM | DMM + tach at 60/120/300 RPM | ~2 / ~4 / ~10 Vrms (baseline model) |
| Loaded LED | series 100 Ω | glow by ~100–150 RPM |
| Gap sensitivity | spacer / reprint | Voc falls as gap ↑ |
| Cogging | feel / stall torque | stronger with dual magnets |
| R_coil | DMM | tens of ohms (sim ~50 Ω @ 26 AWG) |

Compare to `sim/voc_vs_rpm.png`. Large misses → check polarity map, turns count, rubs, or gap.

---

## Optimum simple build (picked)

- Dual Ø20×5, P=8, 2 mm gaps, 26 AWG, locked dual-rotor / fixed stator  
- Skip Ø3 cans, skip 3-phase for v3 (single-phase series is enough for LED lab)
