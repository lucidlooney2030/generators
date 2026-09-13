include <parameters.scad>

// Fixed coil former / stator between magnet drums
// Split into 2 halves for assembly (print twice or mirror)

module stator_half(mirror_xz = false) {
    m = mirror_xz ? -1 : 1;
    difference() {
        union() {
            // Annular half
            intersection() {
                difference() {
                    cylinder(h = coil_axial, r = r_coil_outer);
                    translate([0, 0, -0.1])
                        cylinder(h = coil_axial + 0.2, r = r_coil_inner);
                    // Winding window recess (outer groove)
                    translate([0, 0, 2])
                        difference() {
                            cylinder(h = coil_axial - 4, r = r_coil_outer + 0.1);
                            cylinder(h = coil_axial - 4, r = r_coil_outer - coil_radial + 1.5);
                        }
                }
                translate([-0.1, m >= 0 ? -0.1 : -200, -0.1])
                    cube([200, 200.2, coil_axial + 0.2]);
            }
            // Mounting foot
            translate([r_coil_outer - 2, m * (r_coil_outer - 5), 0])
                cube([28, 10, 6]);
        }
        // Wire exit slot
        translate([r_coil_outer - 1, m * 2, coil_axial / 2 - 1.5])
            cube([8, 6, 3]);
        // Foot screw holes
        translate([r_coil_outer + 10, m * (r_coil_outer), -0.1])
            cylinder(h = 7, d = m3_clear);
        translate([r_coil_outer + 20, m * (r_coil_outer), -0.1])
            cylinder(h = 7, d = m3_clear);
        // Alignment peg holes
        for (z = [4, coil_axial - 4])
            translate([0, 0, z]) rotate([90, 0, 0])
                cylinder(h = 6, d = 2.2, center = true);
    }
}

module stator_bobbin_both() {
    // Export as one file with both halves side by side
    translate([-r_coil_outer - 5, 0, 0]) stator_half(false);
    translate([r_coil_outer + 5, 0, 0]) stator_half(true);
}
stator_bobbin_both();
