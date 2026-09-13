# SCHEMATIC — AFPM-Desk-v1 Wiring & Magnet Polarity

Educational Faraday-induction generator. Low-voltage only. No mains.

---

## 1. Magnet polarity layout (rotor face view)

Looking at the **magnet face** of `rotor_disk` (pockets toward you).  
8 magnets on PCD 70 mm. **Alternate N / S.**

```
                 M1 (N)
                   |
          M8 (S)   |   M2 (S)
             \     |     /
              \    |    /
               \   |   /
        M7 (N) -----●----- M3 (N)
               /   |   \
              /    |    \
             /     |     \
          M6 (S)   |   M4 (S)
                   |
                 M5 (N)
```

- Even indices in OpenSCAD (0,2,4,6) → **N** (bar etch on back of disk).  
- Odd indices (1,3,5,7) → **S** (cross etch).  
- Use `magnet_polarity_jig.stl` during epoxy.

**Rule:** Adjacent magnets must oppose. Same-facing neighbors cancel useful flux change.

---

## 2. Stator coil positions

6 coils, indexed C0…C5, angularly offset +30° from magnet zero so coils sit between pole centers at rest (reduces detent at park; still continuous EMF when spinning).

```
              C0
               |
        C5     |     C1
           \   |   /
            \  |  /
      C4 ---- ● ---- C2
            /  |  \
           /   |   \
        C3     |     
```

**Wind direction:** All coils wound the **same way** on the former (e.g. clockwise when viewing from rotor). Mark start (dot) and finish leads.

---

## 3. Recommended first wiring — series single string → bridge → LED

Simplest for first light:

```
  C0s ── C0f──┐
              ├── C1s ── C1f ──┐
                               ├── … (series all 6) …
                                              └── C5f ──●── AC1
  C0 start = AC2 ●──────────────────────────────────────┘

  AC1 ────┐         ┌──── (+) ─── 220–470Ω ─── LED ─── (−)
          │  BRIDGE │
  AC2 ────┤  RECT   ├──── (−) ─────────────────────────────┘
          └─────────┘
```

ASCII bridge (classic diamond):

```
          AC1
           │
      ┌────┴────┐
      │         │
     D1▷       ◁D2
      │         │
     (+)       (−)
      │         │
     D3▷       ◁D4
      │         │
      └────┬────┘
           │
          AC2
```

Diode orientation: cathodes of D1/D2 toward (+); anodes of D3/D4 toward (−).  
Module packages (W04M) already wire this; ~1.4 V total forward drop — significant at LED voltages, so series-aid coils matter.

---

## 4. Better educational wiring — 3-phase (v1 optional)

Group coils 120° apart:

| Phase | Coils (series) |
|-------|----------------|
| A | C0 + C3 |
| B | C1 + C4 |
| C | C2 + C5 |

Connect phase finishes (or starts — be consistent) in **star (Y)**: join one end of A,B,C; take other ends to a **3-phase bridge** (or 6 discrete diodes).  
Star neutral can float for LED experiments.

Phase EMF ≈ 2× single-coil EMF (series aiding if wound same sense and spaced correctly).

---

## 5. Measurement taps

```
  [Coil string] ──┬── DMM ACV (open circuit)
                  │
                  ├── Bridge ── DMM DCV / LED load
                  │
                  └── Scope CH1 (optional AC waveform)
```

Tachometer on crank or phone RPM app on rotor mark.

---

## 6. Mechanical stack (side view)

```
   CRANK ═╤════ SHAFT ════╤═ HUB ═ ROTOR+MAGNETS
          │               │              ↕ air gap 2–3 mm
       BRG│            BRG│           STATOR+COILS
          │               │              │
        ══╧══ BASE PLATE ═╧══════════════╧══
                         │
                   ELECTRONICS TRAY (rectifier, LED)
```

---

## 7. Polarity check procedure

1. Spin slowly by hand with DMM on ACV across one coil.  
2. Note voltage.  
3. If series pair **decreases** V when connected, reverse one coil’s leads (series opposing → fix to series aiding).

---

## 8. SVG

See also `schematics/wiring_polarity.svg` for a printable diagram.

---
*End SCHEMATIC — AFPM-Desk-v1*
