# PHYSICS — Coax Faraday v3

Educational estimates. **Reject perpetual motion / overunity / “magnets alone make free power.”**  
Mechanical work against Lenz drag → electrical energy (+ heat).

---

## 1. Governing equations

\[
\mathcal{E} = -N\frac{d\Phi_B}{dt}
\]

For approximately sinusoidal flux:

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

Baseline \(P=8\) → \(f=4\times(\mathrm{RPM}/60)\). At 120 RPM, \(f=8\,\mathrm{Hz}\).

---

## 2. Magnet material (citations)

**Assumption:** magnets are **Ø20 mm × 5 mm axial discs**, grade **N42** preferred (N52 optional).

| Grade | Br (typical) | Hcb / Hcj (order) | Sources |
|-------|--------------|-------------------|---------|
| **N42** | **1.28–1.32 T** (use **1.30 T**) | Hcb ~860–955 kA/m; Hcj ≥955 kA/m | [supermagnete S-20-05-N datasheet](https://www.supermagnete.nl/eng/data_sheet_S-20-05-N.pdf); [MPCO N42 20×5](https://mpcomagnetics.com/product/20-x-5mm-round-disk-neodymium-iron-boron-magnet-n42-ni/); [Newland typical properties](https://newlandmagnetics.eu/wp-content/uploads/2020/06/typical-magnetic-properties.pdf) |
| **N52** | **1.42–1.48 T** (use **1.44 T**) | lower Hcj than N42 (~876 kA/m min band) | [Arnold N52](https://www.arnoldmagnetics.com/wp-content/uploads/2017/11/N52-151021.pdf); [Eclipse NdFeB grades](https://www.eclipsemagnetics.com/site/assets/files/33708/em_ca_neodymium_grades_datasheet.pdf); [Goudsmit grades](https://www.goudsmitmagnetics.com/uploads/pdf/Neodymium_grades_available_at_Goudsmit_20250822_1547.pdf) |

Ø3×5 mm cans use the **same grade Br**; only geometry (area / permeance) changes.

Gap flux **≠ Br**. Remanence is a material property; useful \(B_g\) depends on reluctance of air gaps + coil path + leakage.

---

## 3. Topology & polarity

**Chosen:** outer + inner magnet drums **locked** → one rotor; **coil cylinder fixed** (stator).  
Justification: no brushes; radial flux through stationary copper; dual magnets raise \(B_g\); desk-safe.

**Polarity map (P=8):** looking along shaft, stations \(0^\circ,45^\circ,\ldots\):

| Angle | Outer face (toward coil) | Inner face (toward coil) |
|-------|--------------------------|---------------------------|
| 0° | **N** (N-in) | **N** (N-out) |
| 45° | **S** | **S** |
| 90° | **N** | **N** |
| … | alternate | alternate |

Facing pair at each station: **like poles toward the coil** so flux goes outer→coil→inner (or reverse) **radially**, then returns azimuthally via adjacent opposite poles. Equivalent: treat each station as a radial “through-coil” pair with alternating sign around the circle.

---

## 4. Geometry & assumptions (baseline)

| Item | Value |
|------|-------|
| Inner magnet face radius | 33 mm |
| Air gap each side | 2 mm (sweep 1–3 mm) |
| Coil radial depth | 9 mm |
| Outer magnet face radius | ≈46 mm |
| Magnet | Ø20×5 mm, \(A_m=\pi(0.01)^2=3.14\times10^{-4}\,\mathrm{m}^2\) |
| Axial active | ≈22–24 mm |
| Coupling \(k_c\) | 0.70 (dual) |
| Leakage / fringing factor in Bg model | ~0.55 (dual) |

**Bg model (dual):**

\[
B_g \approx B_r\cdot\frac{L_{m,\mathrm{eff}}}{L_{m,\mathrm{eff}}+g_{\mathrm{eff}}}\cdot k_{\mathrm{leak}}
\]

with \(L_{m,\mathrm{eff}}\approx 2\times5\,\mathrm{mm}\), \(g_{\mathrm{eff}}\approx 2\cdot\mathrm{gap}+\mathrm{coil\_radial}\).  
Baseline result: **\(B_g\approx0.31\,\mathrm{T}\)** (N42, 2 mm gaps).

\[
\Phi_{\mathrm{peak}}\approx k_c B_g A_m \approx 6.8\times10^{-5}\,\mathrm{Wb}
\]

**Single-magnet (no inner)** drops \(B_g\) and FoM roughly **2–3×** in this model — dual is worth the cogging.

---

## 5. Inner magnet choice (calculation)

| Option | P (fit) | Φ order | FoM \(P\cdot\Phi\) (sim) |
|--------|---------|---------|-------------------------|
| Dual Ø20 inner + Ø20 outer | 8 | ~6.8e-5 Wb | **~5.5e-4** ← **WIN** |
| Dual Ø3 inner + Ø20 outer | up to 12 | ~1.5e-6 Wb | ~1.8e-5 |
| Outer only | 8 | ~2.5e-5 Wb | ~2.0e-4 |

**Pick Ø20×5 inner discs.** Smaller cans allow more poles in isolation, but outer Ø20 already sets P; area loss dominates.

**Tradeoffs acknowledged:** dual magnets raise \(B_g\) but increase **cogging / attractive forces** (pinch hazard). Coils need radial thickness for copper fill vs gap reluctance.

---

## 6. Simulation results (`sim/`)

Script: `sim/coax_faraday_v3.py` → `sweep_results.csv`, `voc_vs_rpm.png`, `iled_vs_rpm.png`, `voc_vs_gap.png`.

**Baseline @ 120 RPM** (P=8, gap=2 mm, 26 AWG, dual Ø20):

| Voc rms | Voc peak | f | N (approx) | R coil | I_LED est |
|---------|----------|---|------------|--------|-----------|
| **~4.1 V** | **~5.9 V** | 8 Hz | ~500 | ~50 Ω | **~17 mA** |

Ø3 inner same conditions: Voc rms **~0.09 V** (LED off).

Sweep covers poles {6,8,10}, gaps 1–3 mm, AWG {28,26}, RPM 60–600, both inner sizes.

FEMM not required; analytical + numpy is sufficient for desk sizing.

---

## 7. Safety

- **Pinch:** dual neo drums snap together violently — assemble with spacers, keep fingers clear, use non-ferrous tools.
- **Shatter:** NdFeB is brittle; epoxy fully in pockets; eye protection when handling.
- **Voltage:** desk-safe low V; still avoid shorted turns while cranking hard (heating + strong drag).
- **Children / pets:** choke hazard; strong magnets.
- **No mains** connection in this design.

---

## 8. What “success” means

Lit LED / measurable Voc on a multimeter while feeling Lenz drag. That is Faraday’s law — not free power.
