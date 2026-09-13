# PHYSICS_NOTE — HF-RF16-SERP 16P/16S

Orthodox Faraday estimate only. No exotic claims.

## Machine class

- **Radial flux**, **outer rotor**: magnets on the **inner** cylindrical wall of a rotating cup.
- Flux crosses the **1.00 mm** air gap **radially** into the stator.
- Coil **active length is axial** (20 mm groove span), not circumferential pancakes.
- **16 poles / 16 slots**, single-phase **serpentine (wave)** winding with pitch = pole pitch = **22.5°**.
- Stator has **open grooves / lands (no ferromagnetic teeth)**; mild-steel tube provides flux return at the bore.

## Why EMF appears

Each magnet pole sweeps past an axial conductor once per pole pitch. For a single axial run of length ℓ in a radial field B_r at radius R, the motional EMF is on the order of:

\[
e \sim B_r\,\ell\,v = B_r\,\ell\,(\omega R)
\]

With N_turns series wave turns (each turn ≈ two axial runs for a full go-and-return across the machine, depending on count), AC EMF scales as:

\[
E_{\mathrm{rms}} \sim k\,N\,B_r\,\ell\,R\,\omega
\]

Electrical frequency: \(f_e = N_p\,n_{\mathrm{rev}}\) with \(N_p = 8\) pole-**pairs** (16 poles) → \(f_e = 8\,n\) (rev/s).

## Order-of-magnitude (sanity, not a promise)

Assume:

| Symbol | Rough value |
|---|---|
| B_r in gap | 0.3–0.6 T (NdFeB Ø20×5 behind ~1 mm gap + sleeve; no iron teeth → toward low end) |
| ℓ active | ~0.020 m |
| R | ~0.056 m |
| N | 80–120 turns |
| ω | 157 rad/s (≈1500 rpm) |

Then per-turn peak ~ BℓωR ≈ 0.4×0.02×157×0.056 ≈ **0.07 V**, ×100 turns × coupling factor ~0.3–0.6 (single-phase serpentine, leakage without teeth) → **low single-digit to low tens of volts** open-circuit at that speed. Power is modest; this is a learning / light-duty PMG, not a multi-kW machine.

Rectify with a full-wave bridge and bulk capacitor (≥1000 µF) for DC experiments.

## Design implications called out

1. **No stator teeth** → higher reluctance / leakage than a slotted iron stator; B_r and coupling are deliberately conservative above.
2. **Steel tube at bore r≈47** is the main flux return; lands are printed polymer.
3. **Outer rotor** keeps magnet mass at larger radius (good for inertia / turbine coupling) with centrifugal seating into pocket floors.
4. Serpentine single-phase → pulsating torque / ripple; expect vibration vs. a three-phase machine.

All estimates are classical Faraday / Lorentz; validate on the bench with a known rpm and scope.
