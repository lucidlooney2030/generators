include <parameters.scad>

// Inner rotor drum: Ø20×5 discs, faces OUTWARD, alternating poles
module magnet_pocket_outward(ang) {
    rotate([0, 0, ang])
        translate([inner_drum_core_r, 0, drum_axial / 2])
            rotate([0, 90, 0])
                cylinder(h = magnet_h + magnet_pocket_z + 0.2,
                         d = magnet_d + magnet_pocket_xy, center = false);
}

module inner_magnet_drum() {
    difference() {
        union() {
            // Barrel
            cylinder(h = drum_axial, r = inner_drum_core_r + 0.2);
            // End flanges
            cylinder(h = 3, r = inner_drum_core_r + 4);
            translate([0, 0, drum_axial - 3])
                cylinder(h = 3, r = inner_drum_core_r + 4);
        }
        // Shaft bore (slip on hub)
        translate([0, 0, -0.1])
            cylinder(h = drum_axial + 0.2, d = shaft_d + clearance_slip);
        // Magnet pockets — radial outward
        for (i = [0:pole_count - 1])
            magnet_pocket_outward(i * 360 / pole_count);
        // Set-screw flats / M3 tap holes on flange
        for (a = [0, 180])
            rotate([0, 0, a]) translate([0, 0, 1.5])
                rotate([0, 90, 0]) cylinder(h = inner_drum_core_r + 5, d = m3_tap);
    }
}
inner_magnet_drum();
