include <parameters.scad>
od = 28;
id = shaft_d + clearance_loose;

module spacer_ring(thickness=1.0) {
  difference() {
    cylinder(h=thickness, d=od);
    translate([0,0,-0.1])
      cylinder(h=thickness+0.2, d=id);
  }
}
