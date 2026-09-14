include <parameters.scad>
// Print FIRST. Hole ladder, bearing seats, magnet+pole-shoe pockets, screw pilots.

module fit_coupon() {
  difference() {
    cube([95, 55, 8]);

    // shaft hole ladder: +0.2 .. +0.5
    for (i = [0:3]) {
      d = shaft_d + 0.2 + i*0.1;
      translate([12 + i*16, 12, -0.1])
        cylinder(h=8.2, d=d);
    }

    // bearing pocket variants: OD-0.2, OD-0.15, OD-0.1
    for (i = [0:2]) {
      d = bearing_od - 0.2 + i*0.05;
      translate([15 + i*24, 38, 8 - bearing_h + 0.01])
        cylinder(h=bearing_h, d=d);
    }

    // magnet pocket (Ø20×5)
    translate([78, 12, 8 - magnet_h - magnet_pocket_z])
      cylinder(h=magnet_h + 0.25, d=magnet_d + magnet_pocket_xy);

    // pole-shoe pocket (Ø18×2)
    translate([78, 38, 8 - pole_shoe_h - pole_shoe_pocket_z])
      cylinder(h=pole_shoe_h + 0.25, d=pole_shoe_d + pole_shoe_pocket_xy);

    // M3 clearance / tap
    translate([90, 12, -0.1]) cylinder(h=8.2, d=m3_clear);
    translate([90, 22, -0.1]) cylinder(h=8.2, d=m3_tap);
  }
}

fit_coupon();
