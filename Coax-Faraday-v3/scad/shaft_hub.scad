include <parameters.scad>

// Shaft hub: keys inner drum + clamps to shaft; mates closed end of outer drum
module shaft_hub() {
    difference() {
        union() {
            cylinder(h = 10, d = 24);
            // Pilot into inner drum
            cylinder(h = 18, d = shaft_d + 6);
            // Flange to outer closed end
            translate([0, 0, 0]) cylinder(h = 3, d = 30);
        }
        translate([0, 0, -0.1])
            cylinder(h = 18.2, d = shaft_d + 0.15);
        // M3 clamp / set screw
        translate([0, 0, 12]) rotate([0, 90, 0])
            cylinder(h = 15, d = m3_tap);
        // Bolt circle matches outer drum closed end
        for (a = [0:60:300])
            rotate([0, 0, a]) translate([12, 0, -0.1])
                cylinder(h = 3.2, d = m3_clear);
    }
}
shaft_hub();
