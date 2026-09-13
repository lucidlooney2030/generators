# SCHEMATIC — Polarity & Wiring (v3)

## Mechanical topology

```
        rotating together (ROTOR)              fixed (STATOR)
   ┌─────────────────────────────┐         ┌──────────────┐
   │ Outer drum  Ø20×5  (N/S)in  │         │              │
   │         ↓ radial flux        │←—gap—→ │  Copper coil │←—gap—→ Inner drum Ø20×5 (N/S)out
   │                              │         │   bobbin     │
   └────────── shaft_hub / end_cap / shaft ─┴──────────────┘
                         608 bearings on base
```

Outer + inner mechanically locked via `shaft_hub` + `rotor_end_cap` on common Ø8 shaft.  
Coil cylinder bolted to base — **no brushes**.

---

## Polarity map (P=8)

View along +shaft. Stations every 45°.

```
        0° OUTER:N-in     INNER:N-out
       /    \
  315° S     N 45°
       |  COIL |
  270° N     S 90°
       \    /
      225°   135°
        180° OUTER:N-in   INNER:N-out
```

**Rule:** at each station, outer face polarity = inner face polarity (both toward coil), then **alternate** around the circle.  
Flux path: outer face → radial through coil → inner face → return via adjacent opposite pole pair.

Use `polarity_jig.stl`: tall peg = N seat, short peg = S seat (or label with marker).

---

## Coil wiring (single-phase — default)

Wind the stator window as **one continuous coil** (or P concentrated sectors **in series**, same sense relative to alternating poles).

```
[Coil start]----+----[Bridge ~]----+----[100 Ω]----[LED+]
                |                  |
[Coil end]------+----[Bridge ~]    +----[LED−]----gnd/return
                     [Bridge +]--------------------┘
                     [Bridge −]---- system return
```

- Bridge: W04M/W04G or 4×1N4007  
- LED: 2 V class; series **100 Ω** (tune 47–220 Ω)  
- For Voc measurement: disconnect LED; measure AC across coil or DC after bridge

**Series sectors (optional):** 8 slots → connect so voltages add at the electrical frequency \(f=\mathrm{RPM}/60\cdot P/2\).

---

## 3-phase (optional, not required)

If you wind 3 groups at 120° electrical (for P=8, 60° mechanical between groups):

```
  A ──┐
  B ──┼── star or delta ──→ 3-ph bridge → DC rail
  C ──┘
```

v3 BOM/sim assume **single-phase** for simplicity.

---

## Desk-safe notes

- Open-circuit volts are low (single-digit to low teens at hand crank)  
- Do **not** connect to mains  
- Shorted coil while cranking → strong drag + heating
