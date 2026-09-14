// AFPM-Desk-v4 PoleShoe shared parameters (mm)
// SSDR dual-rotor axial-flux PM learning generator:
// mild-steel back-iron + mild-steel pole shoes under each magnet.
// Faraday induction education only — not free-energy / overunity.
// Target: Anycubic Kobra 3 Max, 0.4 mm nozzle, 0.2 mm layers, PETG.

$fn = 72;

// --- Printer / FDM assumptions ---
nozzle = 0.4;
layer = 0.2;
wall = 1.6;                 // load-bearing ~4 perimeters
housing_wall = 2.4;
clearance_slip = 0.35;      // shaft slip fit
clearance_loose = 0.55;
press_interference = 0.15;  // bearing pocket undersize total (coupon-test)
magnet_pocket_xy = 0.25;    // +0.25 mm on diameter
magnet_pocket_z = 0.15;     // +0.15 mm depth
elephant_foot = 0.5;

// --- Magnets (N42 Neo discs) — Austin's Ø20×5 stock ---
magnet_d = 20;
magnet_h = 5;
magnet_count = 12;          // per rotor (12+12 total)
magnet_pcd = 90;            // center pitch; ~3.3 mm edge gap between discs

// --- Mild-steel pole shoes (flux concentrators under each magnet) ---
// Slightly smaller OD than magnet teaches concentration / reluctance.
pole_shoe_d = 18;
pole_shoe_h = 2.0;          // purchased mild-steel disc or punched blank
pole_shoe_pocket_xy = 0.30;
pole_shoe_pocket_z = 0.15;

// --- Steel back-iron (purchased mild steel disc behind pole-shoe ring) ---
steel_od = 118;
steel_id = 16;              // clearance around hub boss
steel_h = 1.5;              // 1.5–2.0 mm mild steel OK
steel_recess_clearance = 0.3;

// --- Rotor printed disc ---
rotor_od = 130;
rotor_hub_bore = 12;        // seats on shaft_hub boss
rotor_thickness = 11;       // magnet + pole shoe + plastic floor + steel recess
magnet_pocket_depth = magnet_h + magnet_pocket_z;
pole_shoe_pocket_depth = pole_shoe_h + pole_shoe_pocket_z;
steel_recess_depth = steel_h + 0.2;

// --- Stator (coreless, between rotors) — 9 coils for 3-phase ---
stator_od = 140;
stator_id = 30;
stator_thickness = 12;
coil_count = 9;
coil_slot_w = 22;
coil_slot_l = 28;           // radial length of pocket
coil_slot_depth = 10;
coil_pcd = 90;
stator_pillar_pcd = 118;    // M4 pillar holes

// --- Coil bobbin (stays in stator) ---
former_core_w = 16;
former_core_l = 24;
former_flange = 2.5;
former_wind_h = 9.2;        // fits coil_slot_depth - margin

// --- Shaft / bearings ---
shaft_d = 8;
bearing_od = 22;            // 608-2RS / 608ZZ
bearing_id = 8;
bearing_h = 7;
bearing_seat_od = bearing_od - press_interference; // ~21.85; coupon-test

// --- Base / frame ---
base_w = 200;
base_d = 180;
base_h = 8;
post_h = 78;
post_spacing = 145;         // Y distance between bearing post centers (thicker stack)
post_d = 36;

// --- Axial stack targets ---
// crank | brg | hub+rotorA+steel | air | stator | air | steel+rotorB+hub | brg
air_gap_nominal = 1.75;     // mechanical per side magnet↔coil face (1.5–2.0)

// --- Crank ---
crank_arm_len = 90;
crank_arm_w = 18;
crank_arm_t = 10;
handle_d = 14;
handle_len = 45;

// --- Electronics tray ---
tray_w = 80;
tray_d = 55;
tray_h = 14;

// --- Fasteners ---
m3_clear = 3.4;
m3_tap = 2.5;
m4_clear = 4.3;
