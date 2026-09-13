include <parameters.scad>

// Removable end cap: locks outer drum to shaft (mechanically couples outer+inner rotors)
module rotor_end_cap() {
    od = outer_drum_od - 1;
    difference() {
        union() {
            cylinder(h = 5, d = od);
            // Hub boss
            cylinder(h = 14, d = 22);
        }
        // Shaft bore
        translate([0, 0, -0.1])
            cylinder(h = 14.2, d = shaft_d + clearance_slip);
        // M3 set screw
        translate([0, 0, 9]) rotate([0, 90, 0])
            cylinder(h = 12, d = m3_tap);
        // Bolt circle to outer drum open end — use perimeter tabs
        for (a = [0, 120, 240])
            rotate([0, 0, a]) translate([od / 2 - 4, 0, -0.1])
                cylinder(h = 5.2, d = m3_clear);
        // Lightening / clearance for stator foot swing during assembly
        for (a = [30, 150, 270])
            rotate([0, 0, a]) translate([od / 2 - 12, 0, -0.1])
                cylinder(h = 5.2, d = 16);
    }
}
rotor_end_cap();
