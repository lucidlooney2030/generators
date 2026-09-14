# PHYSICS — AFPM-Desk-v4 PoleShoe

Educational estimates. **Reject perpetual motion / overunity / “magnets alone make free power.”**  
Mechanical work against Lenz drag → electrical energy (+ heat).

Assumptions stated. **No fabricated lab measurements** — order-of-magnitude from standard EM relations + cited material properties. Validate with a DMM/tach on your build.

---

## 1. Governing equations

\[
\mathcal{E} = -N\frac{d\Phi_B}{dt}
\]

For approximately sinusoidal flux through one coil:

\[
\Phi(t)\approx\Phi_{\mathrm{peak}}\sin(2\pi f t)
\quad\Rightarrow\quad
\mathcal{E}_{\mathrm{peak}}\approx N\cdot 2\pi f\cdot\Phi_{\mathrm{peak}}
\]

\[
\mathcal{E}_{\mathrm{rms}}\approx\mathcal{E}_{\mathrm{peak}}/\sqrt{2}
\]

Electrical frequency for \(P\) poles:

\[
f=\frac{\mathrm{RPM}}{60}\cdot\frac{P}{2}
\]

**v4:** \(P=12\) → \(f=6\times(\mathrm{RPM}/60)\).

| RPM | \(f\) (Hz) |
|-----|------------|
| 60  | 6 |
| 90  | 9 |
| 120 | **12** |
| 180 | 18 |

(Refs: synchronous-machine frequency relation; AFPM modelling e.g. Gieras; [MDPI Energies 13(21):5741](https://www.mdpi.com/1996-1073/13/21/5741).)

---

## 2. Magnet material

**Assumption:** Ø20×5 mm axial N42 discs (Austin stock).

| Grade | Br (typical) | Sources |
|-------|--------------|---------|
| **N42** | **1.28–1.32 T** (use **1.30 T**) | [supermagnete S-20-05-N](https://www.supermagnete.nl/eng/data_sheet_S-20-05-N.pdf); manufacturer N42 bands |

Gap flux **≠ Br**. Remanence is a material property; useful \(B_g\) depends on reluctance of air + coil path + leakage + steel return.

---

## 3. Topology & flux path

```
[steel back-iron A][pole shoe][magnet A Ø20×5]
        -- air gap (~1.75 mm) --
              [coil / plastic]
        -- air gap (~1.75 mm) --
[magnet B Ø20×5][pole shoe][steel back-iron B]
```

- Facing magnets **N↔S** across stator → axial flux through coils.
- Adjacent magnets on one rotor **alternate** N/S.
- **Back-iron:** low-reluctance circumferential return (classic SSDR AFPM).
- **Pole shoes (Ø18×2 mild steel under each magnet):** locally lower reluctance and teach **flux concentration / reluctance** — shoes do not create energy; they reshape the magnetic circuit.

Coreless stator (no iron teeth): smoother hand crank, thicker effective magnetic gap than slotted industrial AFPM.

---

## 4. Air-gap flux density model (assumptions)

Non-steel path (order of magnitude):

| Segment | Thickness |
|---------|-----------|
| Magnet A | 5 mm |
| Mechanical air A | ~1.5–2.0 mm (use 1.75) |
| Coil / plastic stator | ~10 mm effective |
| Mechanical air B | ~1.75 mm |
| Magnet B | 5 mm |

Crude series-reluctance estimate (µ_gap ~ 1):

\[
B_g \approx B_r\cdot\frac{L_{m,\mathrm{eff}}}{L_{m,\mathrm{eff}}+g_{\mathrm{eff}}}\cdot k_{\mathrm{leak}}
\]

with \(L_{m,\mathrm{eff}}\approx 2\times 5\,\mathrm{mm}\), \(g_{\mathrm{eff}}\approx 2\cdot\mathrm{gap}+\mathrm{coil\_axial}\), and \(k_{\mathrm{leak}}\approx 0.65\) (dual + steel + shoes; conservative).

| Case | \(B_g\) (model) |
|------|-----------------|
| v2-like (3 mm mags, steel, no shoes) | ~0.23 T (same formula) |
| v4 no shoes (5 mm + steel) | ~0.32 T |
| **v4 + pole shoes (baseline)** | **~0.36 T** |
| Upper teaching band (less leakage) | ~0.45–0.55 T |

**Central conservative estimate used below: \(B_g = 0.36\,\mathrm{T}\).**  
Upper band ~0.50 T if shoes + steel couple better than the crude leak factor — treat as a sensitivity case, not a measured value.

Magnet face area:

\[
A_m=\pi(0.010)^2=3.14\times10^{-4}\,\mathrm{m}^2
\]

Coupling coil vs magnet footprint \(k_c\approx 0.70\) (9 coils / 12 poles fractional alignment):

\[
\Phi_{\mathrm{peak}}\approx k_c B_g A_m
\approx 0.70\times 0.36\times 3.14\times10^{-4}
\approx 7.9\times10^{-5}\,\mathrm{Wb}
\]

(Upper band Φ ≈ \(1.1\times10^{-4}\) Wb at \(B_g=0.50\,\mathrm{T}\).)

**vs v2:** thicker magnets + higher pole count + shoes raise \(f\) and improve Φ relative to a like-for-like reluctance model; absolute Voc also depends on turns and wiring.

---

## 5. Turns & resistance (LED demo recommendation)

| Item | Recommendation |
|------|----------------|
| Wire | **28 AWG** enamel Cu (~0.32 mm bare; ~0.213 Ω/m @ 20 °C typical) |
| Turns / coil | **~200** hand-wind target (bobbin window allows more if filled carefully) |
| Mean turn length | ≈ 0.08 m (24×16 mm core rectangle) |
| \(R_{\mathrm{coil}}\) | ≈ **3.4 Ω** @ 200 turns |

Alt: **26 AWG**, ~150 turns → lower R, easier LED current, slightly lower Voc.

---

## 6. Open-circuit voltage estimates

### One coil @ 120 RPM (\(f=12\,\mathrm{Hz}\), \(N=200\), Φ = 7.9×10⁻⁵ Wb)

\[
\mathcal{E}_{\mathrm{peak,1}}\approx 200\cdot 2\pi\cdot 12\cdot 7.9\times10^{-5}\approx 1.19\,\mathrm{V}
\]

\[
\mathcal{E}_{\mathrm{rms,1}}\approx 0.84\,\mathrm{V}
\]

Upper band (\(B_g=0.50\,\mathrm{T}\)): ~**1.1–1.2 Vrms** / coil.

### Scale with RPM (∝ f ∝ RPM)

| RPM | \(f\) | Voc rms / coil (cons.) |
|-----|-------|-------------------------|
| 60 | 6 | ~0.42 V |
| 120 | 12 | ~**0.84 V** |
| 180 | 18 | ~1.3 V |

### Wiring aggregates @ 120 RPM (rough)

| Config | Expectation OC |
|--------|----------------|
| Single coil | ~0.8–1.2 Vrms |
| 1 phase = 3 coils series | ~**2.5–3.5 Vrms** |
| Y line-line | ~**4–6 Vrms** (√3 × phase, ideal) |
| All series (careful aiding) | higher, phase-risk if wrong |

**Hand-crank band (60–180 RPM):** plan on **~1–8 Vrms** open-circuit depending on wiring — **LED-scale after rectification**, not utility voltage.

`sim/afpm_desk_v4.py` reproduces these curves (`voc_vs_rpm.png`, `sweep_results.csv`).

Diode bridge drop (~0.6–1.4 V) is significant at LED voltages — use Schottky.

---

## 7. Rough power

Example: rectified ~3 V into LED drawing 20–50 mA → \(P\sim 0.06\)–\(0.15\,\mathrm{W}\).  
Vigorous crank / smaller gap / denser winding → **~0.5–2 W** educational ballpark.

\[
P_{\mathrm{elec}} < P_{\mathrm{mech}}=\tau\omega
\]

Copper \(I^2R\), bearing friction, windage, and eddy/hysteresis in back-iron + pole shoes all reduce η. At hand RPM, steel eddy is modest if discs are thin (1.5–2 mm).

---

## 8. What pole shoes do *not* do

- Do **not** create energy from magnets alone.
- Do **not** enable self-running / overunity.
- Do **not** violate Faraday or Kelvin–Planck.
- They reshape reluctance so **more of your crank work** couples into \(d\Phi/dt\) (and a bit more steel loss).

---

## 9. Safety (magnetic)

- Dual **12+12 N42 Ø20×5** arrays: **severe pinch/crush**. Assemble with spacers; never put fingers in the gap.
- Non-magnetic tools; keep steel tools away from open faces.
- NdFeB shatter risk — eye protection; epoxy fully.
- Desk-safe low V electrically; still avoid hard shorts while cranking.

---

## 10. Citations & further reading

1. Faraday’s law — Griffiths *Introduction to Electrodynamics*; any intro EM text.
2. [Modeling of Axial Flux Permanent Magnet Generators](https://www.mdpi.com/1996-1073/13/21/5741) — Energies 13(21):5741 (2020).
3. Latoufis et al. — DIY AFPM sizing for small wind (12-pole / 9-coil practice).
4. Habib et al., SSDR coreless AFPM — *Alexandria Engineering Journal* (2024).
5. N42 NdFeB \(B_r\) — manufacturer datasheets (e.g. supermagnete S-20-05-N).
6. Reluctance / permeance methods — standard machine design texts (Gieras *Axial Flux Permanent Magnet Brushless Machines*).

Nuance: published AFPM papers often target kW machines; **scaling laws apply**, but absolute V/I here are desk-learning.

---

## 11. Measurement plan

1. Tach / phone RPM on rotor mark.
2. DMM ACV one coil vs RPM → slope ∝ \(N\Phi\).
3. Scope frequency → confirm \(f=6\cdot\mathrm{RPM}/60\).
4. Vary gap with spacer rings → Voc falls as gap rises.
5. Optional: compare Voc with vs without pole shoes (same magnets/gap) — expect modest rise with shoes if leakage was significant.

---
*End PHYSICS — AFPM-Desk-v4 PoleShoe*
