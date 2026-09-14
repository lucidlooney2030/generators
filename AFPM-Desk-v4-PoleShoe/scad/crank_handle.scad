include <parameters.scad>

module crank_handle() {
  difference() {
    union() {
      cylinder(h=handle_len, d=handle_d);
      cylinder(h=3, d=handle_d + 6);
    }
    translate([0,0,-0.1])
      cylinder(h=handle_len+0.2, d=m4_clear);
  }
}

crank_handle();
