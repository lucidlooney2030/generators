include <parameters.scad>

module hand_crank() {
    difference() {
        union() {
            // Hub
            cylinder(h = crank_arm_t, d = 22);
            // Arm
            translate([0, -crank_arm_w / 2, 0])
                cube([crank_arm_len, crank_arm_w, crank_arm_t]);
            // Handle boss
            translate([crank_arm_len, 0, 0])
                cylinder(h = crank_arm_t + 4, d = handle_d + 4);
        }
        // Shaft bore
        translate([0, 0, -0.1])
            cylinder(h = crank_arm_t + 0.2, d = shaft_d + 0.2);
        // Set screw
        translate([0, 0, crank_arm_t / 2]) rotate([0, 90, 0])
            cylinder(h = 14, d = m3_tap);
        // Handle hole (dowel / printed pin)
        translate([crank_arm_len, 0, -0.1])
            cylinder(h = crank_arm_t + 4.2, d = handle_d - 1);
    }
}
hand_crank();
