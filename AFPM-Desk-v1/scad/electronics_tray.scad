include <parameters.scad>

module electronics_tray() {
  difference() {
    cube([tray_w, tray_d, tray_h]);
    translate([2, 2, 2])
      cube([tray_w - 4, tray_d - 4, tray_h]);
    // bridge rectifier pocket
    translate([8, 8, 1])
      cube([20, 20, 3]);
    // LED / banana jack holes
    translate([50, 15, -0.1])
      cylinder(h=tray_h+0.2, d=8);
    translate([50, 35, -0.1])
      cylinder(h=tray_h+0.2, d=8);
    // wire notch
    translate([-0.1, tray_d/2 - 3, tray_h - 4])
      cube([4, 6, 5]);
  }
}

electronics_tray();
