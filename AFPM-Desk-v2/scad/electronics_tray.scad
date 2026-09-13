include <parameters.scad>

module electronics_tray() {
  difference() {
    cube([tray_w, tray_d, tray_h]);
    translate([2,2,2])
      cube([tray_w-4, tray_d-4, tray_h]);
    // rectifier pocket
    translate([8, 8, 1])
      cube([20, 12, 4]);
    // LED holes
    for (i = [0:3]) {
      translate([40 + i*7, tray_d/2, -0.1])
        cylinder(h=3, d=5.2);
    }
    // banana jack holes
    translate([10, tray_d - 12, -0.1]) cylinder(h=3, d=8);
    translate([25, tray_d - 12, -0.1]) cylinder(h=3, d=8);
  }
}

electronics_tray();
