include <parameters.scad>
// Optional clamp washer for M4 stator pillars. Print 3–6.

module stator_clamp() {
  difference() {
    cylinder(h=3, d=18);
    translate([0,0,-0.1])
      cylinder(h=3.2, d=m4_clear);
  }
}

stator_clamp();
