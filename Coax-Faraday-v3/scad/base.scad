include <parameters.scad>

module bearing_post(y) {
    translate([0, y, 0]) {
        difference() {
            union() {
                // Post body
                translate([-post_d / 2, -post_d / 2, 0])
                    cube([post_d, post_d, post_h]);
                // Fillet feet
                hull() {
                    translate([-post_d / 2 - 8, -post_d / 2, 0]) cube([post_d + 16, post_d, 4]);
                    translate([-post_d / 2, -post_d / 2, 0]) cube([post_d, post_d, 12]);
                }
            }
            // Bearing seat (axis at z = post_h - 12)
            translate([0, 0, post_h - 12])
                rotate([90, 0, 0])
                    cylinder(h = post_d + 2, d = bearing_seat_od, center = true);
            // Through shaft clearance tunnel
            translate([0, 0, post_h - 12])
                rotate([90, 0, 0])
                    cylinder(h = post_d + 2, d = 12, center = true);
            // Cap screw holes
            for (x = [-10, 10])
                translate([x, 0, post_h - 2])
                    cylinder(h = 4, d = m3_clear);
        }
    }
}

module base() {
    difference() {
        union() {
            // Floor
            translate([-base_w / 2, -base_d / 2, 0])
                cube([base_w, base_d, base_h]);
            bearing_post(-post_spacing / 2);
            bearing_post(post_spacing / 2);
            // Stator mount rail (center)
            translate([-20, -15, base_h])
                cube([40, 30, 4]);
        }
        // Stator foot holes
        for (xy = [[-10, -8], [10, -8], [-10, 8], [10, 8]])
            translate([xy[0], xy[1], base_h - 1])
                cylinder(h = 6, d = m3_clear);
        // Weight-save cutouts
        for (x = [-50, 50])
            translate([x, 0, -0.1])
                cylinder(h = base_h + 0.2, d = 30);
    }
}
base();
