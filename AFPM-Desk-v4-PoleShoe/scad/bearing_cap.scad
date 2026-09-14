include <parameters.scad>
// Print 2. Retains 608ZZ in post seats.

module bearing_cap() {
  difference() {
    union() {
      cylinder(h=3, d=post_d - 2);
      cylinder(h=bearing_h + 2, d=bearing_od - 1);
    }
    translate([0,0,-0.1])
      cylinder(h=bearing_h + 2.2, d=shaft_d + 1.5);
    for (a = [0,120,240]) {
      rotate([0,0,a])
        translate([12, 0, -0.1])
          cylinder(h=3.2, d=m3_clear);
    }
  }
}

bearing_cap();
