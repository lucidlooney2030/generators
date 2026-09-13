include <parameters.scad>

// Axial spacer / shim between hub and drum — set THICKNESS via -D
thickness = 2.0;
module spacer_ring() {
    difference() {
        cylinder(h = thickness, d = 28);
        translate([0, 0, -0.1]) cylinder(h = thickness + 0.2, d = shaft_d + 1);
    }
}
spacer_ring();
