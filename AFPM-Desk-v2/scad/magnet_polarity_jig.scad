include <parameters.scad>

module magnet_polarity_jig() {
  difference() {
    cylinder(h=4, d=rotor_od - 4);
    translate([0,0,-0.1])
      cylinder(h=4.2, d=30);
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, 1])
          cylinder(h=3.2, d=magnet_d + 0.4);
    }
  }
  // geometric N (bar) / S (cross) markers for rotor-A pattern
  for (i = [0:magnet_count-1]) {
    angle = i * 360 / magnet_count;
    is_N = (i % 2 == 0);
    rotate([0,0,angle])
      translate([magnet_pcd/2 + 15, 0, 4]) {
        if (is_N) {
          cube([8, 1.6, 1.2], center=true);
        } else {
          cube([8, 1.6, 1.2], center=true);
          cube([1.6, 8, 1.2], center=true);
        }
      }
  }
}

magnet_polarity_jig();
