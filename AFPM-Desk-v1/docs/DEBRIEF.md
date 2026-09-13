# DEBRIEF — Generator Experiments v1 (AFPM-Desk)

**Build name:** AFPM-Desk-v1  
**Type:** Hand-crank **axial-flux permanent-magnet** educational generator  
**Physics basis:** Faraday’s law of induction (orthodox; not free-energy)  
**Audience:** Austin Carolino — desktop learning build  
**Date package:** 2026-09-07 (America/New_York)

---

## 1. Why this design (selection rationale)

Candidates considered:

| Option | Pros | Cons for desk v1 |
|--------|------|------------------|
| Brushed DC motor as dynamo | Cheap, fast | High RPM needed; weak educational “magnet+coil” story |
| Faraday disk (homopolar) | Historic | Tiny volts; brush noise; hard LED demo |
| Reciprocating coil+magnet | Simple | Pulsed, low average power, awkward crank coupling |
| **Axial-flux PM (chosen)** | Clear flux change, 3D-printable, LEDs at hand speed, classic DIY pedagogy | Magnet pinch hazard; coil winding time |

**Chosen:** single-rotor / single-stator **axial-flux PM generator** with hand crank, optional small DC-motor drive later. Dual-rotor sandwich is a natural v2 upgrade (higher B_g).

Educational payoff: visible magnet polarity pattern, measurable AC vs RPM, cogging feel, rectifier → LED, compare measurements to Faraday estimates below.

---

## 2. Parts identified (labeled)

| Label | Part | Role |
|-------|------|------|
| R1 | `rotor_disk.stl` | Carries 8 N42 discs; rotates; provides changing B |
| S1 | `stator_mount.stl` | Holds 6 coils fixed relative to base |
| B1 | `base_plate.stl` | Desk frame; bearing posts; stator pillars |
| H1 | `shaft_hub.stl` | Couples 8 mm shaft ↔ rotor |
| C1/C2 | `hand_crank.stl` + `crank_handle.stl` | Human mechanical input |
| BRG | 2× 608 bearings | Low-friction shaft support |
| CAP | `bearing_cap.stl` ×2 | Bearing retention |
| CF | `coil_former.stl` | Winding jig for ~200-turn coils |
| ET | `electronics_tray.stl` | Rectifier + LED / jacks |
| JIG | `magnet_polarity_jig.stl` | Ensures alternating N/S |
| SP | `spacer_ring.stl` | Sets ~2–3 mm air gap during setup |
| M1–M8 | N42 Ø20×3 mm Neo discs | Permanent magnet poles |
| W1–W6 | Magnet-wire coils | EMF pickup (Faraday) |
| SHAFT | Ø8×~180 mm steel rod | Mechanical axis |
| RECT | W04M / DB107 bridge | AC→DC for LEDs |
| LOAD | LEDs + series resistor | Visible output |

---

## 3. Bill of materials (approximate sources / USD)

Prices are ballpark US hobby retail (Amazon / Digi-Key / McMaster / local hardware), 2026 order of magnitude.

| Qty | Item | Spec | Approx. | Notes |
|-----|------|------|---------|-------|
| 8 | Neo disc magnets | **N42**, Ø20 mm × 3 mm, Ni-plated | $8–15 / pack | Prefer N42; N52 OK but stronger pinch |
| 1 spool | Magnet wire | **28 AWG** enameled Cu, ≥100 m | $10–15 | 26 AWG = fewer turns / lower V |
| 2 | Ball bearings | **608-2RS** (8×22×7 mm) | $3–6 | Skateboard bearings |
| 1 | Shaft | Steel rod Ø8 mm × 180–200 mm | $3–8 | Cut + deburr |
| 4 | Set screws | M3 × 6 mm | $2 | Hub + crank |
| 8 | Screws | M3 × 12 mm + nuts | $2 | Hub↔rotor |
| 3 | Screws | M4 × 35 mm + nuts/standoffs | $3 | Stator↔base pillars |
| 1 | Bridge rectifier | 1 A / 50–400 V (W04M etc.) | $1–2 | Overkill voltage OK |
| 5–10 | LEDs | 5 mm red/green + 220–470 Ω resistors | $2 | Load demo |
| 2 | Banana jacks (opt.) | Panel 4 mm | $3 | Measurement |
| 1 | Multimeter | Any DMM with ACV/DCV | — | Essential |
| — | Filament | PLA or PETG ~150–200 g | $5 | All STLs |
| 1 | Cyanoacrylate / epoxy | Gel CA or 5-min epoxy | $5 | Magnet + coil potting |
| 1 | Kapton / electrical tape | — | $3 | Coil finishing |
| 1 | Eye protection | Safety glasses | — | **Required** with Neos |

**Total hardware (excl. printer/meter):** roughly **$45–80**.

---

## 4. Geometry assumptions (as printed)

From `scad/parameters.scad`:

- Rotor OD 100 mm; magnet PCD 70 mm; **8 poles**
- Magnets Ø20 × 3 mm in pockets ~3.2 mm deep
- Stator OD 110 mm; **6 coil** pockets on PCD 70 mm
- Shaft Ø8 mm; bearings 608
- Design mechanical **air gap** target: **2.0–3.0 mm** (rotor face ↔ coil face)
- Coil former core ≈ racetrack ~14×26 mm, wind height ~10–11 mm → ~200 turns of 28 AWG is realistic

---

## 5. Physics notes (double-checked, orthodox)

### 5.1 Faraday’s law

\[
\mathcal{E} = -N \frac{d\Phi_B}{dt}
\]

For approximately sinusoidal flux through one coil:

\[
\Phi(t) \approx \Phi_{\mathrm{peak}} \sin(2\pi f t), \quad
\mathcal{E}_{\mathrm{peak}} \approx N \cdot 2\pi f \cdot \Phi_{\mathrm{peak}}
\]

\[
\mathcal{E}_{\mathrm{rms}} \approx \frac{\mathcal{E}_{\mathrm{peak}}}{\sqrt{2}}
\]

Electrical frequency for an alternator with \(P\) poles:

\[
f = \frac{\mathrm{RPM}}{60} \cdot \frac{P}{2}
\]

Here \(P = 8\) → \(f = (\mathrm{RPM}/60)\times 4\).

| RPM (hand/motor) | \(f\) (Hz) |
|------------------|------------|
| 60 | 4 |
| 120 | 8 |
| 300 | 20 |
| 600 | 40 |

### 5.2 Magnet grade & air-gap flux (assumptions)

- **N42** NdFeB remanence \(B_r \approx 1.28\)–\(1.32\,\mathrm{T}\) (typical datasheet band).
- Single-sided rotor (no steel back-iron in v1 plastic disk): flux return is poor → **air-gap flux density facing a coil is much less than \(B_r\)**.
- Conservative working assumption for estimates:

\[
B_g \approx 0.25\text{–}0.40\,\mathrm{T}
\]

at ~2–3 mm gap over the magnet face (order-of-magnitude; measure with a gaussmeter if available). Adding a thin steel backing plate behind magnets (v1.1) raises \(B_g\) toward ~0.5 T — optional upgrade, increases cogging.

Magnet face area:

\[
A_m = \pi (0.010)^2 = 3.14\times 10^{-4}\,\mathrm{m}^2
\]

Peak flux linkage estimate per coil (magnet fully aligned; coupling factor \(k_c \approx 0.6\)–\(0.8\) for finite coil size):

\[
\Phi_{\mathrm{peak}} \approx k_c B_g A_m
\approx 0.7 \times 0.30 \times 3.14\times 10^{-4}
\approx 6.6\times 10^{-5}\,\mathrm{Wb}
\]

### 5.3 Turns & wire

- **28 AWG** diameter ≈ 0.32 mm bare; with enamel ~0.33–0.35 mm.
- ~200 turns fit on the coil former (verify by counting while winding).
- DC resistance per coil (length ≈ 200 × ~0.08 m mean turn ≈ 16 m):

\[
R_{\mathrm{coil}} \approx 16\,\mathrm{m} \times 0.213\,\Omega/\mathrm{m} \approx 3.4\,\Omega
\]

(28 AWG ≈ 0.213 Ω/m at 20 °C — use datasheet if available.)

### 5.4 Expected EMF (order of magnitude)

One coil at **120 RPM** (\(f=8\,\mathrm{Hz}\)):

\[
\mathcal{E}_{\mathrm{peak,1}} \approx 200 \times 2\pi \times 8 \times 6.6\times 10^{-5}
\approx 0.66\,\mathrm{V}
\]

\[
\mathcal{E}_{\mathrm{rms,1}} \approx 0.47\,\mathrm{V}
\]

Wiring options:

1. **All 6 coils in series (single-phase style, educational):**  
   Open-circuit \(\mathcal{E}_{\mathrm{rms,total}} \sim 2.5\)–\(4\,\mathrm{V}\) at ~120 RPM (phases don’t peak together — treat as rough; expect **~1.5–3 Vrms** measured depending on series phasing).  
   Better: wire as **3-phase** (two coils series per phase, 120° spatial) then 3-phase bridge; phase EMF ~ **0.8–1.5 Vrms** @ 120 RPM, more at higher RPM.

2. **Practical desk targets:**
   - Hand crank ~60–150 RPM → **~0.5–4 V** open-circuit AC (config dependent), enough to **flash/light LEDs** after rectification if series stacking is correct.
   - Small DC motor / drill at 300–600 RPM → roughly **linear scale with RPM**: expect **several volts** OC; still keep loads LED-scale.

**Current:** short-circuit / LED current limited by coil R and rectifier. Expect **tens of mA** into LEDs at hand speed — measurable, not hazardous. Do **not** connect to mains or battery banks without proper engineering (out of scope).

### 5.5 Power & energy honesty

Mechanical input power \(P_{\mathrm{mech}} = \tau\omega\). Electrical output \(P_{\mathrm{elec}} = VI\) with \(\eta < 1\) due to copper loss, bearing friction, windage, hysteresis/eddy if steel added. **Electrical energy out never exceeds mechanical energy in.**

---

## 6. Safety

1. **Neodymium pinch hazard** — fingers can be blood-blistered between magnets or magnet↔steel. Slide magnets into pockets; never let two free magnets slam.
2. **Eye protection** — Neos can chip; plating shards are sharp.
3. **Keep away from pacemakers, magstripe cards, HDDs, phones** during handling.
4. **No mains wiring** — this is isolated low-voltage educational gear only.
5. **Drill drive caution** — if chucking the shaft in a drill, use low speed; overspeed increases voltage and mechanical risk (rotor imbalance).
6. **Children** — adult supervision; magnets are ingestion hazard (medical emergency if swallowed).

---

## 7. Assembly steps

1. **Print** all STLs; clean magnet pockets and bearing seats.
2. **Press 608 bearings** into base posts; add bearing caps loosely.
3. **Mark polarity** of each N42 with a known reference magnet; use `magnet_polarity_jig`.
4. **Epoxy magnets** into rotor pockets with **alternating N/S** (even indices N, odd S as etched). Cure fully.
5. **Bolt shaft hub** to rotor; slide onto shaft; set-screw hub.
6. **Wind 6 coils** on former: ~200 turns 28 AWG; leave 15 cm leads; tape; carefully remove from split former.
7. **Sand enamel** off lead ends; tin with solder.
8. **Seat coils** in stator pockets (same wind direction for series stacking); hot-glue or epoxy lightly.
9. **Mount stator** on base pillars with M4; use `spacer_ring` stack to set **2–3 mm** gap to magnet faces; verify spin clearance (**no scrape**).
10. **Install crank** on shaft end; check smooth rotation and cogging.
11. **Wire** per `SCHEMATIC.md` (start: all coils series → bridge → LED+resistor).
12. **First test:** multimeter ACV while cranking; then connect LED load.

---

## 8. What to measure

| Measurement | Instrument | Expectation |
|-------------|------------|-------------|
| Open-circuit \(V_{\mathrm{ac}}\) vs RPM | DMM ACV + tach/phone RPM | Roughly ∝ RPM |
| Frequency | Scope / phone scope app | \(f = 4\times(\mathrm{RPM}/60)\) |
| Rectified \(V_{\mathrm{dc}}\) no load | DMM DCV | ~0.9× peak AC minus diode drops |
| LED current | DMM mA series | Tens of mA hand speed |
| Coil resistance | DMM Ω | ~3–5 Ω each |
| Air gap | Feeler / calipers | 2–3 mm |
| Cogging torque feel | Hand | Stronger if gap shrinks / steel back-iron added |

Lab notebook prompt: plot \(V_{\mathrm{oc}}\) vs RPM; compare slope to Faraday estimate.

---

## 9. Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| No voltage | Enamel not stripped; open coil; wrong meter mode | Continuity check; use ACV |
| Tiny voltage | Huge air gap; magnets same polarity; few turns | Gap 2–3 mm; re-check N/S; recount turns |
| Rotor scrapes | Gap too small; warped print | Add spacers; re-level stator |
| Harsh cogging / won’t turn | Magnets attracted to steel nearby; gap tiny | Remove ferrous clutter; increase gap |
| LED never lights | Series resistor too large; AC phase cancellation | Try one LED+220Ω on rectified DC; re-wire series aiding |
| Magnet flies out | Poor epoxy / no cure | Re-bond; optional pocket lip redesign |
| Bearing seize | Misalignment | Loosen posts; realign shaft |
| Shock from “high V” | Unlikely at hand RPM; possible with drill | Don’t lick terminals; still low energy |

---

## 10. v1.1 / v2 ideas (not in this package)

- Steel backing plate on rotor (higher \(B_g\))
- Dual rotor sandwich (flux through stator both sides)
- 3-phase rectifier PCB
- Belt drive from small DC motor with known RPM for calibration

---

## 11. Explicit non-claims

- Not a free-energy, zero-point, or overunity machine.  
- Not a substitute for utility power.  
- Magnet “self-running” myths are incompatible with Faraday induction + energy conservation as used here.

---
*End DEBRIEF — AFPM-Desk-v1*
