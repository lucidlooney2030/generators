include <parameters.scad>

module base_frame() {
  y1 = -post_spacing/2;
  y2 =  post_spacing/2;

  difference() {
    union() {
      translate([-base_w/2, -base_d/2, 0])
        cube([base_w, base_d, base_h]);

      // bearing posts
      translate([0, y1, base_h]) cylinder(h=post_h, d=post_d);
      translate([0, y2, base_h]) cylinder(h=post_h, d=post_d);

      // stator pillars (3) — height leaves stator mid-gap
      for (a = [0,120,240]) {
        rotate([0,0,a])
          translate([stator_pillar_pcd/2, 0, base_h])
            cylinder(h=42, d=16);
      }

      // electronics ledge
      translate([base_w/2 - tray_w - 8, -tray_d/2, base_h])
        cube([tray_w, tray_d, 3]);
    }

    // bearing seats from top of posts
    translate([0, y1, base_h + post_h - bearing_h])
      cylinder(h=bearing_h+0.15, d=bearing_seat_od);
    translate([0, y2, base_h + post_h - bearing_h])
      cylinder(h=bearing_h+0.15, d=bearing_seat_od);

    // shaft clearance through posts
    translate([0, y1, base_h-0.1])
      cylinder(h=post_h+0.2, d=shaft_d + 1.2);
    translate([0, y2, base_h-0.1])
      cylinder(h=post_h+0.2, d=shaft_d + 1.2);

    // stator pillar M4
    for (a = [0,120,240]) {
      rotate([0,0,a])
        translate([stator_pillar_pcd/2, 0, base_h-0.1])
          cylinder(h=42.3, d=m4_clear);
    }

    // clamp slots
    for (sx = [-1,1], sy = [-1,1]) {
      translate([sx*(base_w/2 - 22), sy*(base_d/2 - 14), -0.1])
        cube([14, 10, base_h+0.2], center=true);
    }

    // cable pass
    translate([base_w/2 - tray_w - 12, 0, base_h-0.1])
      cylinder(h=4, d=8);
  }
}

base_frame();
