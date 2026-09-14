# SCHEMATIC — AFPM-Desk-v4 PoleShoe

## 1. Mechanical stack (axial, along shaft)

```
[crank][608ZZ][hub][rotorA+shoes+magnets][steel A]
        |← ~1.5–2.0 mm air →|
      [stator + 9 coils]
        |← ~1.5–2.0 mm air →|
[steel B][rotorB+shoes+magnets][hub][608ZZ]
```

Nominal air gap each side: magnet face ↔ coil/bobbin face. Tune with `spacer_1mm` / `1p5mm` / `2mm`.

---

## 2. Rotor polarity (P=12)

Looking along shaft toward rotor A stator face. Stations every 30°.

| Station index | Angle | Rotor A face (→ stator) | Rotor B face (→ stator) |
|---------------|-------|-------------------------|-------------------------|
| 0 | 0° | **N** | **S** |
| 1 | 30° | **S** | **N** |
| 2 | 60° | **N** | **S** |
| … | … | alternate | opposite of A |

Facing pair at each station: **N faces S** so axial flux threads the coils. Adjacent magnets on one rotor alternate → circumferential return via back-iron.

Pole shoe under every magnet (both rotors).

Printed etch: bar = N, cross = S (rotor A pattern on jig; rotor B opposite).

---

## 3. Coil map (9 coils)

Coils seated at angles \(20° + i·40°\) (i = 0…8) so pockets sit between/aligned for 12-pole AFPM coupling.

**3-phase grouping (120° electrical):**

| Phase | Coil indices | Mechanical spacing |
|-------|--------------|--------------------|
| **A** | 0, 3, 6 | every 3rd coil |
| **B** | 1, 4, 7 | |
| **C** | 2, 5, 8 | |

Within a phase, series-connect with **aiding** sense (same wind direction relative to flux). If Voc collapses, reverse one coil in the group.

### Star (Y)

```
Phase A ────●
Phase B ────●─── neutral (optional bring-out)
Phase C ────●
```

Line-line Voc ≈ √3 × phase Voc (balanced OC idealization).

### Delta (Δ)

```
A ──●── B
 \     /
  ●───●
    C
```

Higher current capability, lower line V — useful for low-V LED experiments.

---

## 4. LED demo (desk-safe)

```
[Y or Δ phases] → Schottky bridge → C filter (optional 100–470 µF) → Rseries (100–220 Ω) → LED
```

Si bridge (~1.4 V drop) eats much of the LED budget; **Schottky** preferred.

---

## 5. Frequency check

\[
f = \frac{\mathrm{RPM}}{60}\cdot\frac{P}{2} = 6\cdot\frac{\mathrm{RPM}}{60}
\]

| RPM | f (Hz) |
|-----|--------|
| 60 | 6 |
| 120 | 12 |
| 180 | 18 |

Scope one coil: period should match. Wrong f → wrong pole count / mechanical slip (should be locked).

---

## 6. What not to wire

- Do **not** connect to mains.
- Do **not** short all coils while spinning at high RPM (heating + strong drag).
- Do **not** claim self-running / overunity — Lenz drag always costs mechanical power.
