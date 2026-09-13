include <parameters.scad>

// Retainer over 608 seat on base posts — print 2
module bearing_cap() {
    difference() {
        hull() {
            translate([-14, -8, 0]) cube([28, 16, 3]);
            translate([0, 0, 0]) cylinder(h = 3, d = 28);
        }
        // Shaft clearance
        translate([0, 0, -0.1]) cylinder(h = 3.2, d = 12);
        // Screw holes
        for (x = [-10, 10])
            translate([x, 0, -0.1]) cylinder(h = 3.2, d = m3_clear);
    }
}
bearing_cap();
