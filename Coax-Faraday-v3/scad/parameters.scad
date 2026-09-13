// Coax Faraday Generator Experiments v3 — shared parameters (mm)
// Three-layer coaxial: outer magnets + coil stator + inner magnets
// Orthodox Faraday only — mechanical → electrical. No overunity.
// Target: Anycubic Kobra 3 Max, 0.4 mm nozzle, 0.2 mm layers, PETG preferred.

$fn = 72;

// --- Printer / FDM ---
nozzle = 0.4;
layer = 0.2;
wall = 2.0;                 // ≥2 mm walls on drums
housing_wall = 2.4;
clearance_slip = 0.35;
press_interference = 0.15;  // 608 seat undersize total (~0.1–0.2)
magnet_pocket_xy = 0.25;    // +0.25 mm on diameter (within +0.2–0.3)
magnet_pocket_z = 0.15;     // +0.15 mm depth (within +0.1–0.2)

// --- Magnets (ASSUMPTION: Ø20×5 mm N42 axial discs, not bar stock) ---
magnet_d = 20;
magnet_h = 5;
pole_count = 8;             // alternating N/S around circumference

// --- Radial stack (from axis) ---
// Inner magnet FACE at r=33; magnets 5 mm thick → pocket floor at 33-5=28
r_inner_face = 33;
air_gap = 2.0;              // each side (1–3 mm sweep; nominal 2)
coil_radial = 9.0;          // winding depth
r_coil_inner = r_inner_face + air_gap;          // 35
r_coil_outer = r_coil_inner + coil_radial;      // 44
r_outer_face = r_coil_outer + air_gap;          // 46
// Outer magnet pocket floor (further out): face + thickness
r_outer_floor = r_outer_face + magnet_h;        // 51

inner_drum_od = 2 * (r_inner_face);             // face OD before pockets nuance
inner_drum_core_r = r_inner_face - magnet_h;    // 28
outer_drum_id = 2 * r_outer_face;               // clear to faces
outer_drum_od = 2 * (r_outer_floor + wall);     // ~106

axial_magnet = 22;          // pocket axial span (~magnet_d + margin)
coil_axial = 24;
drum_axial = 28;            // outer/inner drum barrel length

// --- Shaft / bearings 608-2RS ---
shaft_d = 8;
bearing_od = 22;
bearing_id = 8;
bearing_h = 7;
bearing_seat_od = bearing_od - press_interference; // ~21.85

// --- Base ---
base_w = 160;
base_d = 140;
base_h = 8;
post_h = 70;
post_spacing = 100;         // bearing center distance along shaft axis (Y)
post_d = 36;

// --- Crank ---
crank_arm_len = 80;
crank_arm_w = 16;
crank_arm_t = 10;
handle_d = 14;
handle_len = 40;

// --- Fasteners ---
m3_clear = 3.4;
m3_tap = 2.5;
m4_clear = 4.3;
