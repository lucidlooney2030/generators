include <parameters.scad>

module crank_handle() {
    difference() {
        cylinder(h = handle_len, d = handle_d);
        translate([0, 0, -0.1])
            cylinder(h = 12, d = 5.2); // M5 or printed pin
    }
}
crank_handle();
