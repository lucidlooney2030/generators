include <parameters.scad>

module electronics_tray() {
  difference() {
    cube([tray_w, tray_d, tray_h]);
    translate([2, 2, 2])
      cube([tray_w-4, tray_d-4, tray_h]);
    translate([-0.1, tray_d/2, 6])
      rotate([0,90,0])
        cylinder(h=3, d=6);
  }
}

electronics_tray();
