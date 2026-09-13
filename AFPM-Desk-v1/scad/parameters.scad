// AFPM-Desk-v1 shared parameters (mm)
// Desktop axial-flux PM learning generator — Faraday induction education only.

$fn = 64;

// --- Magnets (N42 Neo discs) ---
magnet_d = 20;
magnet_h = 3;
magnet_count = 8;
magnet_pcd = 70; // pitch circle diameter

// --- Rotor ---
rotor_od = 100;
rotor_id = 12; // shaft clearance / hub seat
rotor_thickness = 6;
magnet_pocket_clearance = 0.3;
magnet_pocket_depth = magnet_h + 0.2;

// --- Stator ---
stator_od = 110;
stator_id = 30;
stator_thickness = 8;
coil_count = 6;
coil_slot_w = 22;
coil_slot_h = 18;
coil_slot_depth = 6;
coil_pcd = 70;

// --- Shaft / bearings ---
shaft_d = 8;
bearing_od = 22; // 608 skate bearing
bearing_id = 8;
bearing_h = 7;
bearing_seat_od = bearing_od + 0.2;

// --- Base ---
base_w = 160;
base_d = 140;
base_h = 8;
post_h = 55;

// --- Crank ---
crank_arm_len = 80;
crank_arm_w = 16;
crank_arm_t = 8;
handle_d = 12;
handle_len = 40;

// --- Electronics tray ---
tray_w = 70;
tray_d = 50;
tray_h = 12;
