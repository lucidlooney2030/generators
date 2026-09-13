# Generator Experiments v1 — AFPM-Desk Learning Generator

**Owner:** Austin Carolino
**Purpose:** Desktop educational build for **magnetic electricity production via Faraday induction** (generator / alternator principles).
**Not a free-energy / overunity device.** Output energy comes only from mechanical work you put in (hand crank or small motor). Orthodoxy: Maxwell–Faraday induction only.

## What this is

**AFPM-Desk-v1** is a **hand-crank axial-flux permanent-magnet (AFPM) learning generator**:

- One 3D-printed **rotor disk** carries **8× N42 neodymium discs** in alternating N/S polarity.
- A fixed **stator** holds **6 coils** of magnet wire facing the rotor across a small air gap.
- Turning the crank changes magnetic flux through the coils → induced EMF (AC).
- A bridge rectifier makes low-voltage DC for LEDs / measurement.

Desk-scale targets: measurable volts, LED loads, multimeter experiments — not household power.

## Package contents

| Path | Description |
|------|-------------|
| `DEBRIEF.md` | Parts, BOM, assembly, physics notes, measurements, failure modes |
| `SCHEMATIC.md` | Wiring, magnet polarity layout, ASCII diagrams |
| `schematics/wiring_polarity.svg` | Vector schematic |
| `stl/*.stl` | All 3D-printable parts |
| `scad/*.scad` | OpenSCAD sources (editable) |
| `README.md` | This overview |

## Printable parts (STL)

- `base_plate.stl` — desk base with bearing posts + stator pillars
- `rotor_disk.stl` — magnet pockets + polarity etch marks
- `stator_mount.stl` — 6 coil pockets + wire channels
- `shaft_hub.stl` — couples 8 mm shaft to rotor
- `hand_crank.stl` / `crank_handle.stl` — drive
- `bearing_cap.stl` — retaining caps (print 2)
- `coil_former.stl` — winding jig
- `electronics_tray.stl` — rectifier / LED bay
- `magnet_polarity_jig.stl` — N/S placement aid
- `spacer_ring.stl` — 1 mm air-gap spacers (print several)

## Quick start

1. Read **DEBRIEF.md** (safety first — neo magnets pinch and shatter).
2. Print STLs (PLA/PETG, 0.2 mm layers, ≥3 perimeters for rotor/base).
3. Buy BOM items (N42 20×3 mm discs, 28 AWG magnet wire, 608 bearings, etc.).
4. Wind 6 coils (~200 turns each), assemble per DEBRIEF, set **~2–3 mm air gap**.
5. Measure open-circuit AC with a multimeter while cranking; then rectifier → LED.

## Expected learning payoff

- Feel **cogging** as magnets pass coils.
- See **AC** frequency scale with RPM; rectified DC lights LEDs.
- Compare measured V vs Faraday estimates in DEBRIEF.
- Vary air gap / RPM / series-parallel coil wiring and watch EMF change.

## Physics stance (explicit)

This converts **mechanical energy → electrical energy**. Friction, copper I²R, and magnetic drag mean electrical out ≪ mechanical in. There is **no** claim of perpetual motion, free energy, or overunity.

## License / reproducibility

Open, reproducible educational design. Modify OpenSCAD parameters in `scad/parameters.scad` and re-render.

---
*Generator Experiments · Cycle 1 · v1*
