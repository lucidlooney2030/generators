include <parameters.scad>

// Flat ring jig: marks N/S alternating seats for Ø20 discs before epoxy
module polarity_jig() {
    difference() {
        cylinder(h = 3, r = r_inner_face + 8);
        translate([0, 0, -0.1]) cylinder(h = 3.2, r = r_inner_face - magnet_h - 2);
        for (i = [0:pole_count - 1]) {
            rotate([0, 0, i * 360 / pole_count])
                translate([r_inner_face - magnet_h / 2, 0, 1])
                    cylinder(h = 2.2, d = magnet_d + 0.5);
        }
    }
    // Raised N/S bars: even = N marker (taller), odd = S (shorter)
    for (i = [0:pole_count - 1]) {
        rotate([0, 0, i * 360 / pole_count])
            translate([r_inner_face + 3, -1, 3])
                cube([3, 2, (i % 2 == 0) ? 2.0 : 0.8]);
    }
}
polarity_jig();
