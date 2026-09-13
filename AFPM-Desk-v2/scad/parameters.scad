// AFPM-Desk-v2 shared parameters (mm)
// Dual-rotor axial-flux PM learning generator with steel back-iron.
// Faraday induction education only — not free-energy / overunity.
// Target printer: Anycubic Kobra 3 Max, 0.4 mm nozzle, 0.2 mm layers, PLA/PETG.

$fn = 72;

// --- Printer / FDM assumptions ---
nozzle = 0.4;
layer = 0.2;
wall = 1.6;                 // load-bearing walls ~4 perimeters
housing_wall = 2.4;
clearance_slip = 0.35;      // shaft slip fit
clearance_loose = 0.55;
press_interference = 0.15;  // bearing pocket undersize total (coupon-test)
magnet_pocket_xy = 0.25;    // +0.25 mm on diameter
magnet_pocket_z = 0.15;     // +0.15 mm depth
elephant_foot = 0.5;

// --- Magnets (N42 Neo discs) ---
magnet_d = 20;
magnet_h = 3;
magnet_count = 8;           // per rotor (8+8 total)
magnet_pcd = 70;

// --- Steel back-iron (purchased mild steel disc) ---
steel_od = 100;
steel_id = 14;              // clearance around hub boss
steel_h = 1.5;              // 1.5–2.0 mm mild steel OK
steel_recess_clearance = 0.3;

// --- Rotor printed disc ---
rotor_od = 110;
rotor_hub_bore = 12;        // seats on shaft_hub boss
rotor_thickness = 7;        // magnet pocket from face; steel recess on back
magnet_pocket_depth = magnet_h + magnet_pocket_z;
steel_recess_depth = steel_h + 0.2;

// --- Stator (coreless, between rotors) ---
stator_od = 120;
stator_id = 28;
stator_thickness = 10;
coil_count = 6;
coil_slot_w = 24;
coil_slot_l = 30;           // radial length of pocket
coil_slot_depth = 8;
coil_pcd = 70;
stator_pillar_pcd = 100;    // M4 pillar holes

// --- Coil former / bobbin ---
former_core_w = 14;
former_core_l = 26;
former_flange = 3;
former_wind_h = 11;
former_bore = 0;            // solid core, split design via kerf

// --- Shaft / bearings ---
shaft_d = 8;
bearing_od = 22;            // 608-2RS
bearing_id = 8;
bearing_h = 7;
bearing_seat_od = bearing_od - press_interference; // coupon-test; start ~21.85

// --- Base / frame ---
base_w = 180;
base_d = 160;
base_h = 8;
post_h = 70;
post_spacing = 120;         // Y distance between bearing post centers
post_d = 36;

// --- Axial stack targets (along shaft / Y) ---
// crank | brg | hub+rotorA+steel | air | stator | air | steel+rotorB+hub | brg
air_gap_nominal = 2.0;      // mechanical per side magnet↔coil face

// --- Crank ---
crank_arm_len = 85;
crank_arm_w = 18;
crank_arm_t = 10;
handle_d = 14;
handle_len = 45;

// --- Electronics tray ---
tray_w = 75;
tray_d = 55;
tray_h = 14;

// --- Fasteners ---
m3_clear = 3.4;
m3_tap = 2.5;
m4_clear = 4.3;
