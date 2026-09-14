include <parameters.scad>
// Optional separate carrier ring: holds 12 pole shoes for dry-fit / teaching.
// Nominal design embeds shoes in rotor_disc pockets instead.

module pole_shoe_holder() {
  difference() {
    cylinder(h=pole_shoe_h + 1.2, d=magnet_pcd + pole_shoe_d + 8);
    translate([0,0,-0.1])
      cylinder(h=pole_shoe_h + 1.4, d=magnet_pcd - pole_shoe_d - 6);
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, 1.0])
          cylinder(h=pole_shoe_h + 0.3, d=pole_shoe_d + pole_shoe_pocket_xy);
    }
    // index notch
    translate([magnet_pcd/2 + pole_shoe_d/2 + 2, 0, -0.1])
      cylinder(h=pole_shoe_h + 1.4, d=3);
  }
}

pole_shoe_holder();
