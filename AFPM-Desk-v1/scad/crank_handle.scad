include <parameters.scad>

module crank_handle() {
  difference() {
    union() {
      cylinder(h=handle_len, d=handle_d);
      // flange
      cylinder(h=2, d=handle_d + 4);
    }
    translate([0,0,-0.1])
      cylinder(h=handle_len+0.2, d=5.2); // M5 bolt axle
  }
}

crank_handle();
