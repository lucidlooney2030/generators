include <parameters.scad>

module bearing_cap() {
  difference() {
    cylinder(h=3, d=30);
    translate([0,0,-0.1])
      cylinder(h=3.2, d=shaft_d + 1.5);
    // clip over post — shallow lip
    translate([0,0,2])
      cylinder(h=1.1, d=bearing_od + 2);
  }
}

bearing_cap();
