include <parameters.scad>

module coil_former() {
  difference() {
    union() {
      hull() {
        translate([-6, 0, 0]) cylinder(h=12, d=14);
        translate([6, 0, 0]) cylinder(h=12, d=14);
      }
      hull() {
        translate([-6, 0, 0]) cylinder(h=1.5, d=22);
        translate([6, 0, 0]) cylinder(h=1.5, d=22);
      }
      hull() {
        translate([-6, 0, 10.5]) cylinder(h=1.5, d=22);
        translate([6, 0, 10.5]) cylinder(h=1.5, d=22);
      }
      translate([0, 0, 12])
        cylinder(h=20, d=8);
    }
    translate([-20, -0.4, -0.1])
      cube([40, 0.8, 35]);
  }
}

coil_former();
