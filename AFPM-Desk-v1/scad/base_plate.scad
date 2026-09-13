include <parameters.scad>

module base_plate() {
  difference() {
    union() {
      // plate
      translate([-base_w/2, -base_d/2, 0])
        cube([base_w, base_d, base_h]);
      
      // bearing posts (front = crank side, rear = free end)
      translate([0, -45, base_h])
        cylinder(h=post_h, d=32);
      translate([0, 45, base_h])
        cylinder(h=post_h, d=32);
      
      // stator support pillars (3)
      for (a = [0, 120, 240]) {
        rotate([0,0,a])
          translate([55, 0, base_h])
            cylinder(h=28, d=14);
      }
      
      // electronics tray ledge (right side)
      translate([base_w/2 - tray_w - 5, -tray_d/2, base_h])
        cube([tray_w, tray_d, 3]);
    }
    
    // bearing seats (608) — recessed from top of posts
    translate([0, -45, base_h + post_h - bearing_h])
      cylinder(h=bearing_h + 0.1, d=bearing_seat_od);
    translate([0, 45, base_h + post_h - bearing_h])
      cylinder(h=bearing_h + 0.1, d=bearing_seat_od);
    
    // shaft through-holes in posts
    translate([0, -45, base_h - 0.1])
      cylinder(h=post_h + 0.2, d=shaft_d + 1);
    translate([0, 45, base_h - 0.1])
      cylinder(h=post_h + 0.2, d=shaft_d + 1);
    
    // stator pillar M4 tapped holes / clearance
    for (a = [0, 120, 240]) {
      rotate([0,0,a])
        translate([55, 0, base_h - 0.1])
          cylinder(h=28.2, d=4.2);
    }
    
    // desk clamp slots
    translate([-base_w/2 + 15, -base_d/2 + 10, -0.1])
      cube([12, 8, base_h + 0.2]);
    translate([base_w/2 - 27, -base_d/2 + 10, -0.1])
      cube([12, 8, base_h + 0.2]);
    translate([-base_w/2 + 15, base_d/2 - 18, -0.1])
      cube([12, 8, base_h + 0.2]);
    translate([base_w/2 - 27, base_d/2 - 18, -0.1])
      cube([12, 8, base_h + 0.2]);
    
    // cable pass-through
    translate([base_w/2 - tray_w - 10, 0, base_h - 0.1])
      cylinder(h=4, d=8);
  }
}

base_plate();
