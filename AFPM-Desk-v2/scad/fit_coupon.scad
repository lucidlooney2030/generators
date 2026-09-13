include <parameters.scad>
// Print FIRST. Hole ladder, bearing seats, magnet pocket, screw pilots.
// Measure and adjust parameters.scad clearances before full build.

module fit_coupon() {
  difference() {
    translate([0,0,0]) cube([80, 50, 6]);

    // shaft hole ladder: nominal, +0.3, +0.4, +0.5
    for (i = [0:3]) {
      d = shaft_d + 0.2 + i*0.1;
      translate([12 + i*16, 12, -0.1])
        cylinder(h=6.2, d=d);
    }

    // bearing pocket variants: OD-0.2, OD-0.15, OD-0.1
    for (i = [0:2]) {
      d = bearing_od - 0.2 + i*0.05;
      translate([15 + i*22, 35, 6 - bearing_h + 0.01])
        cylinder(h=bearing_h, d=d);
    }

    // magnet pocket
    translate([65, 12, 6 - magnet_h - 0.15])
      cylinder(h=magnet_h + 0.2, d=magnet_d + 0.25);

    // M3 clearance / tap pilots
    translate([65, 35, -0.1]) cylinder(h=6.2, d=m3_clear);
    translate([72, 35, -0.1]) cylinder(h=6.2, d=m3_tap);
  }
  // labels as shallow grooves
  translate([8, 2, 5.5]) cube([2, 1, 0.6]);
}

fit_coupon();
