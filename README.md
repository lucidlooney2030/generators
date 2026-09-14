# Generators

Printable desktop **magnetic generators** by [Austin Carolino](https://github.com/lucidlooney2030).

Educational Faraday machines: mechanical work in → electricity out. **Not** free-energy / overunity devices.

**System / voice-to-parametric process:** [idea-to-print-pipeline](https://github.com/lucidlooney2030/idea-to-print-pipeline)
This repo is the **hardware library** (OpenSCAD + STL + physics notes). New topology work still lands here. Pipeline work (agents, CadQuery port, gates) lands in the system repo.

| Project | Topology | Print first |
|--------|----------|-------------|
| [**HF-RF16-SERP**](HF-RF16-SERP/) | Radial-flux **outer rotor**, 16P/16S single-phase **wave** winding | [`stl/HF-RF16-ONEPLATE.stl`](HF-RF16-SERP/stl/HF-RF16-ONEPLATE.stl) |
| [**AFPM-Desk-v1**](AFPM-Desk-v1/) | Axial-flux, hand-crank, single rotor | `stl/` parts |
| [**AFPM-Desk-v2**](AFPM-Desk-v2/) | Axial-flux dual-rotor SSDR + steel back-iron | `stl/fit_coupon.stl` then parts |
| [**Coax-Faraday-v3**](Coax-Faraday-v3/) | Coaxial dual magnet drums + fixed coil | `stl/fit_coupon.stl` then parts |
| [**AFPM-Desk-v4 PoleShoe**](AFPM-Desk-v4-PoleShoe/) | Axial-flux dual-rotor + steel back-iron + pole shoes, 12+12 / 9-coil 3-phase | `stl/fit_coupon.stl` then parts |

## Printer

Anycubic **Kobra 3 Max** (or similar). Prefer **PETG / ABS / ASA / nylon**. HF-RF16: do **not** use PLA.

## Safety

Neodymium magnets pinch and shatter. Eye protection. Dual-magnet and outer-rotor builds have strong attractive forces — assemble with spacers.

## License

MIT — print, remix, share. Attribution appreciated.
