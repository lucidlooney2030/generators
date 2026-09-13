include <parameters.scad>

// Outer rotor drum (cup): Ø20×5 discs, faces INWARD, alternating poles
// Closed end has bolt circle to rotor_end_cap / shaft lock

module magnet_pocket_inward(ang) {
    // Pocket cut from outside toward axis; face at r_outer_face
    rotate([0, 0, ang])
        translate([r_outer_face - 0.1, 0, drum_axial / 2])
            rotate([0, 90, 0])
                cylinder(h = magnet_h + magnet_pocket_z + 0.3,
                         d = magnet_d + magnet_pocket_xy, center = false);
}

module outer_magnet_drum() {
    od = outer_drum_od;
    id_clear = 2 * r_outer_face - 0.4; // inside clears magnet faces
    difference() {
        union() {
            // Barrel wall
            difference() {
                cylinder(h = drum_axial + 4, d = od); // +4 closed end thickness zone
                translate([0, 0, 4])
                    cylinder(h = drum_axial + 0.2, d = 2 * r_outer_floor - 0.2);
            }
            // Closed end plate
            cylinder(h = 4, d = od);
        }
        // Shaft clearance through closed end (hub bolts around)
        translate([0, 0, -0.1])
            cylinder(h = 4.2, d = 18);
        // Magnet pockets from OD inward
        for (i = [0:pole_count - 1])
            magnet_pocket_inward(i * 360 / pole_count);
        // Extra carve to ensure pockets open to ID
        for (i = [0:pole_count - 1])
            rotate([0, 0, i * 360 / pole_count])
                translate([r_outer_face - 1, 0, drum_axial / 2 + 2])
                    rotate([0, 90, 0])
                        cylinder(h = magnet_h + 3, d = magnet_d + magnet_pocket_xy);
        // M3 bolt circle for end-cap lock (on closed end)
        for (a = [0:60:300])
            rotate([0, 0, a]) translate([12, 0, -0.1])
                cylinder(h = 4.2, d = m3_clear);
        // Open end registration notches (3) for removable end ring
        for (a = [0, 120, 240])
            rotate([0, 0, a]) translate([od / 2 - 3, -2, drum_axial + 1])
                cube([4, 4, 4]);
    }
}
outer_magnet_drum();
