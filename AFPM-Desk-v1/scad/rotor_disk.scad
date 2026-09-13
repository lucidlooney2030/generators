include <parameters.scad>

module rotor_disk() {
  difference() {
    // main disk
    cylinder(h=rotor_thickness, d=rotor_od, center=false);
    
    // hub / shaft bore with flat for set screw alignment mark
    translate([0,0,-0.1])
      cylinder(h=rotor_thickness+0.2, d=rotor_id);
    
    // magnet pockets — alternating N/S (label in DEBRIEF)
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, rotor_thickness - magnet_pocket_depth])
          cylinder(h=magnet_pocket_depth+0.1, d=magnet_d + magnet_pocket_clearance);
    }
    
    // polarity etch marks: + for N pockets (even), - for S (odd) — shallow grooves
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, -0.05]) {
          if (i % 2 == 0)
            cube([6, 1.2, 0.6], center=true); // N mark as bar
          else {
            cube([6, 1.2, 0.6], center=true);
            cube([1.2, 6, 0.6], center=true); // S mark as cross / plus-ish
          }
        }
    }
    
    // M3 mounting holes for shaft hub (4x on 20mm PCD)
    for (a = [0,90,180,270]) {
      rotate([0,0,a])
        translate([10, 0, -0.1])
          cylinder(h=rotor_thickness+0.2, d=3.2);
    }
  }
}

rotor_disk();
