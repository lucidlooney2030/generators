// serpentine_pm_generator.scad
// Dual-magnet serpentine-coil generator, v1
// 16x outer N52 Ø20x5 mm discs, 48x inner N52 ×5x5 mm (groups of 3)
// Serpentine coil former with through-holes for weaving

// ---- Parameters (edit here, regenerate STL) ----
$fn = 64;

// Outer magnets (20 mm dia x 5 mm thick)
OM_D = 20.0;   // magnet diameter
OM_T = 5.0;    // magnet thickness
OM_POCKET_D = 20.40; // clearance
OM_POCKET_D = 20.40;
OM_POCKET_DEPTH = 5.35;
N_OUTER = 16;

// Inner magnets (5 mm dia x 5 mm thick), 3 per group
IM_D = 5.0;
IM_T = 5.0;
IM_POCKET_D = 5.40;
IM_POCKET_DEPTH = 5.35;
N_INNER_GROUPS = 16;
GROUP_SIZE = 3;

// Coil former
CF_HOLE_D = 2.5;   // through-hole for weaving
CF_ROWS = 5;
CF_COLS = 32;      // 16 even (outer) + 16 odd (inner)

// ---- Outer magnet rotor ----
module outer_rotor() {
    difference() {
        cylinder(h=OM_T+2, d=OM_D*N_OUTER*0.62);
        for (i=[0:N_OUTER-1]) {
            a = i*360/N_OUTER;
            translate([cos(a)*OM_D*N_OUTER*0.30, sin(a)*OM_D*N_OUTER*0.30, 1])
                cylinder(h=OM_POCKET_DEPTH, d=OM_POCKET_D);
        }
    }
}

// ---- Inner magnet hub ----
module inner_hub() {
    difference() {
        cylinder(h=IM_T*GROUP_SIZE+2, d=IM_D*N_INNER_GROUPS*0.55);
        for (i=[0:N_INNER_GROUPS-1]) {
            a = i*360/N_INNER_GROUPS;
            for (g=[0:GROUP_SIZE-1]) {
                translate([cos(a)*IM_D*N_INNER_GROUPS*0.26, sin(a)*IM_D*N_INNER_GROUPS*0.26, 1+g*IM_T])
                    cylinder(h=IM_POCKET_DEPTH, d=IM_POCKET_D);
            }
        }
    }
}

// ---- Serpentine coil former (perforated cage) ----
module coil_former() {
    difference() {
        cylinder(h=CF_ROWS*4, d=OM_D*N_OUTER*0.62);
        for (c=[0:CF_COLS-1]) {
            a = c*360/CF_COLS;
            r = OM_D*N_OUTER*0.30;
            for (row=[0:CF_ROWS-1]) {
                translate([cos(a)*r, sin(a)*r, 2+row*4])
                    rotate([90,0,a]) cylinder(h=6, d=CF_HOLE_D);
            }
        }
    }
}

// ---- Stator cap / stand ----
module stator_stand() {
    difference() {
        cylinder(h=10, d=OM_D*N_OUTER*0.70);
        cylinder(h=12, d=22); // 608 bearing pocket
        for (i=[0:2]) {
            a = i*120;
            translate([cos(a)*OM_D*N_OUTER*0.32, sin(a)*OM_D*N_OUTER*0.32, -1])
                cylinder(h=12, d=8);
        }
    }
}

// Render all
outer_rotor();
translate([0,0,30]) inner_hub();
translate([0,0,60]) coil_former();
translate([0,0,90]) stator_stand();
