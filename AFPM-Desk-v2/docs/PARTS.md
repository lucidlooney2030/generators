# PARTS — AFPM-Desk-v2 Labeled List + Debrief

**Build:** Dual-rotor axial-flux PM generator with steel back-iron  
**Date:** 2026-09-10 (ET)

---

## 1. Labeled printable + purchased parts

| Label | File / item | Qty | Role (physics / mechanical) |
|-------|-------------|-----|-----------------------------|
| RA | `rotor_disc_A.stl` | 1 | Holds 8 magnets; etch = N on even indices facing stator |
| RB | `rotor_disc_B.stl` | 1 | Holds 8 magnets; etch inverted so **N faces S** across gap |
| ST | `stator_plate.stl` | 1 | Coreless coil carrier; flux changes through windings |
| BF | `base_frame.stl` | 1 | Desk frame; bearing posts; stator pillars |
| H1/H2 | `shaft_hub.stl` | 2 | Couples Ø8 shaft ↔ each rotor |
| CF | `coil_former.stl` | 1 | Removable winding jig (~200 turns) |
| CB | `coil_bobbin.stl` | 6 | Optional permanent bobbins in stator pockets |
| CR | `hand_crank.stl` | 1 | Mechanical power input arm |
| CH | `crank_handle.stl` | 1 | Rotating grip |
| CAP | `bearing_cap.stl` | 2 | Retains 608 bearings |
| SP1/1.5/2 | `spacer_*.stl` | 4–8 | Sets axial air gaps / stack spacing |
| JIG | `magnet_polarity_jig.stl` | 1 | Alternating N/S placement aid (rotor-A pattern) |
| ET | `electronics_tray.stl` | 1 | Rectifier + LED / jacks bay |
| CL | `stator_clamp.stl` | 3–6 | M4 clamp washers for stator height |
| FC | `fit_coupon.stl` | 1 | **Print first** — clearance calibration |
| M1–M16 | N42 Ø20×3 mm Neo | 16 | Permanent poles (8 per rotor) |
| IRON-A/B | Mild steel disc Ø100×1.5–2 mm | 2 | **Back-iron** return path; raises \(B_g\) |
| W1–W6 | 28 AWG magnet-wire coils | 6 | EMF pickup (Faraday) |
| BRG | 608-2RS bearings | 2 | Low-friction shaft support |
| SHAFT | Steel rod Ø8 × ~220 mm | 1 | Common mechanical axis |
| RECT | Bridge rectifier 1 A+ | 1 | AC→DC for LEDs |
| LOAD | LEDs + 220–470 Ω | several | Visible sink |
| FAST | M3/M4 screws, set screws, nuts | assorted | Assembly |

---

## 2. Why each critical part (debrief)

### Magnets (N42 discs)
Provide near-constant magnetomotive force. Grade N42 balances strength vs cost/pinch hazard (N52 stronger, meaner). Disc shape packs well in printed pockets. **Alternating polarity** on each rotor is mandatory for useful \(d\Phi/dt\).

### Dual rotors (RA/RB)
Two magnet planes facing the stator double the useful axial sources compared with v1’s single plane and enable the classic SSDR flux path through the coils.

### Steel back-iron
Soft magnetic discs behind magnets lower reluctance of the return path between adjacent poles → higher gap flux for the same magnets (see PHYSICS.md). **Not** a permanent magnet; saturates if too thin under strong Neos — 1.5–2 mm mild steel is a desk compromise. Prefer non-stainless magnetic steel (e.g. 1018 / laser-cut CRS). Austenitic stainless is useless as back-iron.

### Coreless stator + coils
Copper links changing flux → EMF. No iron teeth ⇒ less cogging (hand-friendly) but larger effective magnetic gap. ~200 turns of 28 AWG: voltage-oriented educational choice.

### Air-gap spacers
Faraday EMF ∝ flux; flux falls as gap rises. Spacers make the gap a **controlled experimental variable**.

### Shaft, hubs, bearings
Define kinematic axis; hubs lock rotors in angular register so facing N/S pairs stay aligned.

### Crank
Human \(\tau\omega\) source — the only energy input that matters.

### Rectifier / LEDs
Make AC tangible as DC light; diode drop teaches why series-aiding coils matter at low V.

---

## 3. Bill of materials (approx. USD, hobby retail 2026)

| Qty | Item | Spec | Approx. $ | Notes |
|-----|------|------|-----------|-------|
| 16 | Neo discs | N42 Ø20×3 mm Ni-plated | 15–30 | 8 reused from v1 + 8 new |
| 2 | Steel discs | Ø100 mm × 1.5–2 mm mild steel | 8–20 | Laser-cut or saw+file; ID ~14 mm hole |
| 1 spool | Magnet wire | 28 AWG enameled ≥150 m | 10–15 | |
| 2 | Bearings | 608-2RS | 3–6 | |
| 1 | Shaft | Ø8×220 mm steel | 4–10 | Longer than v1 |
| assorted | M3/M4 hardware | set screws, bolts, nuts | 5–10 | |
| 1 | Bridge rectifier | ≥1 A | 1–2 | |
| LEDs+R | 5 mm + resistors | — | 2 | |
| Filament | PLA/PETG | ~250–350 g | 6–10 | Heavier than v1 |
| Adhesive | Epoxy / CA | — | 5 | Magnets + steel |
| Safety glasses | — | — | — | **Required** |

**Total hardware excl. printer/meter:** roughly **$60–110**.

---

## 4. Key dimensions (from `parameters.scad`)

| Parameter | Value |
|-----------|-------|
| Magnet | Ø20 × 3 mm, PCD 70 mm, 8 per rotor |
| Rotor OD | 110 mm; thickness 7 mm |
| Steel | Ø100 × 1.5 mm recess |
| Stator | OD 120 mm; thickness 10 mm; 6 coil pockets |
| Shaft | Ø8 mm |
| Bearings | 608 (8×22×7) |
| Post spacing | 120 mm |
| Base | 180 × 160 × 8 mm |
| Nominal air gap / side | 2.0 mm |

---

## 5. Safety (repeat)

1. Neo **pinch** — dual rotors **attract strongly** across the gap; keep fingers clear when bringing RA/RB near; assemble with spacers already set.  
2. Eye protection — chips.  
3. Pacemakers / cards / HDDs / phones — distance.  
4. No mains. Isolated LV educational only.  
5. Steel discs have sharp edges — deburr.  
6. Adult supervision if minors present; magnet ingestion = emergency.

---
*End PARTS — AFPM-Desk-v2*
