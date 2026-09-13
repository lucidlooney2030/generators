# PHYSICS — AFPM-Desk-v2 Dual-Rotor Sandwich

Educational estimates only. Assumptions stated. **Reject perpetual-motion claims.**

---

## 1. Governing law (Faraday / Lenz)

\[
\mathcal{E} = -N \frac{d\Phi_B}{dt}
\]

Lenz’s law: induced current opposes the flux change that produces it → **magnetic drag** when loaded. You feel that drag in the crank; it is the mechanical power being converted (plus losses).

For approximately sinusoidal flux through one coil:

\[
\Phi(t) \approx \Phi_{\mathrm{peak}}\sin(2\pi f t)
\quad\Rightarrow\quad
\mathcal{E}_{\mathrm{peak}} \approx N\cdot 2\pi f\cdot\Phi_{\mathrm{peak}}
\]

\[
\mathcal{E}_{\mathrm{rms}} \approx \mathcal{E}_{\mathrm{peak}}/\sqrt{2}
\]

Electrical frequency for \(P\) poles:

\[
f = \frac{\mathrm{RPM}}{60}\cdot\frac{P}{2}
\]

Here \(P = 8\) (same pole count as v1 on each rotor) → \(f = 4\times(\mathrm{RPM}/60)\).

| RPM | \(f\) (Hz) |
|-----|------------|
| 60  | 4 |
| 90  | 6 |
| 120 | 8 |
| 300 | 20 |

(Refs: standard synchronous-machine frequency relation; AFPM modelling e.g. Gieras et al.; Energies 2020 “Modeling of Axial Flux Permanent Magnet Generators” [MDPI Energies 13(21):5741](https://www.mdpi.com/1996-1073/13/21/5741).)

---

## 2. Why dual-rotor + steel back-iron raises \(B_g\)

**v1 problem:** single plastic rotor → flux return through air/plastic → large reluctance → \(B_g\) facing coils ≪ \(B_r\).

**v2 path:**

```
[steel A][magnet A] --air-- [coil] --air-- [magnet B][steel B]
```

- Facing magnets at the same angular station are **opposite polarity** (N on A faces S on B) so axial flux threads the coil.
- Adjacent magnets on one rotor **alternate** N/S.
- **Steel back-iron** (mild steel, µ_r ≫ 1) gives a low-reluctance path between adjacent poles on each rotor, concentrating useful gap flux (classic SSDR / dual-rotor AFPM; see also Latoufis et al. rural AFPM design notes; Habib et al. SSDR coreless comparisons, AEJ 2024).

**N42 remanence:** typical datasheet \(B_r \approx 1.28\)–\(1.32\,\mathrm{T}\) (e.g. manufacturer N42 bands). Gap flux is **not** \(B_r\).

---

## 3. Air-gap flux density assumptions (v2)

Magnetic non-steel path (order of magnitude):

| Segment | Thickness |
|---------|-----------|
| Magnet A | 3 mm (source) |
| Mechanical air A | ~2 mm |
| Coil / plastic stator | ~8–10 mm effective |
| Mechanical air B | ~2 mm |
| Magnet B | 3 mm (source) |

Conservative **working assumption** for mid-coil flux density under a magnet face with dual N42 + steel:

\[
B_g \approx 0.40\text{–}0.60\,\mathrm{T}
\]

(Central estimate used below: **\(B_g = 0.50\,\mathrm{T}\)**.  
v1 used ~0.30 T. Dual + steel ≈ **~1.5–2×** coupling improvement — not infinite.)

If a gaussmeter is available, measure at mid-gap with stator removed / thin probe — revise Φ below.

Magnet face area (Ø20 mm):

\[
A_m = \pi (0.010)^2 = 3.14\times 10^{-4}\,\mathrm{m}^2
\]

Coupling factor coil vs magnet footprint \(k_c \approx 0.65\)–\(0.80\) (coil window ≠ magnet disc exactly):

\[
\Phi_{\mathrm{peak}} \approx k_c B_g A_m
\approx 0.75 \times 0.50 \times 3.14\times 10^{-4}
\approx 1.18\times 10^{-4}\,\mathrm{Wb}
\]

---

## 4. Turns & resistance

- Wire: **28 AWG** enameled Cu (~0.32 mm bare; ~0.213 Ω/m @ 20 °C typical).
- Target: **~200 turns / coil** on former (same as v1 skill).
- Mean turn length ≈ 0.08 m → length ≈ 16 m → \(R_{\mathrm{coil}} \approx 3.4\,\Omega\).

More turns → higher EMF **and** higher R (and harder to fit). Fewer turns (26 AWG) → lower V, higher current capability.

---

## 5. Open-circuit voltage estimates

### One coil @ 120 RPM (\(f = 8\,\mathrm{Hz}\))

\[
\mathcal{E}_{\mathrm{peak,1}} \approx 200 \cdot 2\pi \cdot 8 \cdot 1.18\times 10^{-4}
\approx 1.18\,\mathrm{V}
\]

\[
\mathcal{E}_{\mathrm{rms,1}} \approx 0.84\,\mathrm{V}
\]

### @ 60 RPM (\(f = 4\,\mathrm{Hz}\)) — scale ∝ RPM

\[
\mathcal{E}_{\mathrm{rms,1}} \approx 0.42\,\mathrm{V}
\]

### Wiring aggregates (rough)

| Config | Expectation @ 120 RPM OC |
|--------|---------------------------|
| Single coil | ~0.7–1.0 Vrms |
| 2 coils series aiding (one phase) | ~1.4–2.0 Vrms |
| 3-phase star, phase-phase | ~2–4 Vrms (geometry/phasing dependent) |
| All 6 series (careful aiding) | ~3–6 Vrms possible; phase cancellation if wrong |

**Hand-crank band (60–120 RPM):** plan on **~1–8 Vrms** open-circuit depending on wiring — **LED-scale after rectification**, not utility voltage.

**Drill @ 300 RPM:** ~2.5× the 120 RPM numbers → still typically **low tens of volts max** if heavily series-stacked; treat as educational, not grid.

Diode bridge drops ~1.4 V (Si) — significant at LED voltages; Schottky helps.

---

## 6. Rough power

Loaded, \(P \approx V I\) with I limited by coil R + load.

Example: rectified ~3 V into LED string drawing 50 mA → \(P \approx 0.15\,\mathrm{W}\).  
Vigorous crank / better wiring / smaller gap → **~0.5–2 W** educational ballpark.  
With motor drive at higher RPM, a few watts possible — still **order of watts**, desk-safe energy.

**Energy honesty:**

\[
P_{\mathrm{elec}} < P_{\mathrm{mech}} = \tau\omega
\]

Copper loss \(I^2R\), bearing friction, windage, and (with steel) some eddy/hysteresis in back-iron all reduce η. Steel should be **thin** (1.5–2 mm) and preferably **laminated or low-carbon** to limit eddy; for hand RPM eddy is modest.

---

## 7. What dual-rotor does *not* do

- Does **not** create energy from magnets alone.
- Does **not** run itself from its own output (Lenz drag + losses).
- Does **not** violate Faraday or Kelvin–Planck.
- Stronger magnets / steel only improve **coupling** of the mechanical input you provide.

---

## 8. Citations & further reading

1. Faraday’s law — any intro EM text (Griffiths *Introduction to Electrodynamics*).
2. [Modeling of Axial Flux Permanent Magnet Generators](https://www.mdpi.com/1996-1073/13/21/5741) — Energies 13(21):5741 (2020): dual-rotor disc AFPM analytical models, coreless vs cored stator.
3. Latoufis et al., “Axial flux permanent magnet generator design for low cost manufacturing of small wind turbines” — practical DIY AFPM sizing (magnet grade, gap, turns). PDF: rurerg.net / related Scoraig/Otherpower lineage.
4. Habib et al., SSDR vs DSSR coreless AFPM prototype comparison — *Alexandria Engineering Journal* (2024): SSDR enables fully coreless path, higher power density for portable apps.
5. Analytical ironless AFPM sizing (N42 example parameters) — Electronics 2025, “Analytical Modeling of an Ironless Axial Flux Machine…” [MDPI Electronics](https://www.mdpi.com/2079-9292/14/14/2901).
6. N42 NdFeB typical \(B_r\) — manufacturer datasheets (e.g. 1.28–1.32 T).

Nuance: published AFPM papers often target kW wind machines; **scaling laws still apply**, but absolute V/I here are desk-learning, not turbine-rated.

---

## 9. Measurement plan (validate estimates)

1. Tach or phone RPM on rotor mark.
2. DMM ACV on one coil vs RPM → slope ∝ \(N\Phi\).
3. Scope frequency → confirm \(f = 4\cdot\mathrm{RPM}/60\).
4. Vary air gap with spacer rings → V falls as gap rises (reluctance).
5. Compare v1 single-rotor (if retained) vs v2 dual at same RPM/gap — expect higher V on v2.

Lab notebook: plot \(V_{\mathrm{oc}}\) vs RPM; annotate assumed \(B_g\).

---
*End PHYSICS — AFPM-Desk-v2*
