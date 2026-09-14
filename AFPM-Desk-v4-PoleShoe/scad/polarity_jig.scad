include <parameters.scad>
// Assembly jig: 12 magnet stations with N/S etch for rotor-A pattern.
// Rotor B uses opposite facing polarity across the gap (N faces S).

module polarity_jig() {
  difference() {
    cylinder(h=4, d=rotor_od - 4);
    translate([0,0,-0.1])
      cylinder(h=4.2, d=32);
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, 1])
          cylinder(h=3.2, d=magnet_d + 0.4);
    }
  }
  for (i = [0:magnet_count-1]) {
    angle = i * 360 / magnet_count;
    is_N = (i % 2 == 0);
    rotate([0,0,angle])
      translate([magnet_pcd/2 + 16, 0, 4]) {
        if (is_N) {
          cube([8, 1.6, 1.2], center=true);
        } else {
          cube([8, 1.6, 1.2], center=true);
          cube([1.6, 8, 1.2], center=true);
        }
      }
  }
}

polarity_jig();
