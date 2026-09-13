include <parameters.scad>
// Library module — use rotor_disc_A.scad / rotor_disc_B.scad to export.

module rotor_disc(side="A") {
  difference() {
    cylinder(h=rotor_thickness, d=rotor_od);

    // hub bore
    translate([0,0,-0.1])
      cylinder(h=rotor_thickness+0.2, d=rotor_hub_bore);

    // magnet pockets on FRONT face
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, rotor_thickness - magnet_pocket_depth])
          cylinder(h=magnet_pocket_depth+0.15, d=magnet_d + magnet_pocket_xy);
    }

    // steel plate recess on BACK face
    translate([0,0,-0.05])
      difference() {
        cylinder(h=steel_recess_depth+0.05, d=steel_od + steel_recess_clearance);
        cylinder(h=steel_recess_depth+0.1, d=steel_id);
      }

    // polarity etch (visible before steel install)
    // Rotor A: even index N facing stator; Rotor B: opposite so N faces S across gap
    for (i = [0:magnet_count-1]) {
      angle = i * 360 / magnet_count;
      is_N = (side == "A") ? (i % 2 == 0) : (i % 2 == 1);
      rotate([0,0,angle])
        translate([magnet_pcd/2, 0, steel_recess_depth + 0.35]) {
          if (is_N) {
            cube([7, 1.4, 0.7], center=true);
          } else {
            cube([7, 1.4, 0.7], center=true);
            cube([1.4, 7, 0.7], center=true);
          }
        }
    }

    // M3 hub holes
    for (a = [0,90,180,270]) {
      rotate([0,0,a])
        translate([10, 0, -0.1])
          cylinder(h=rotor_thickness+0.2, d=m3_clear);
    }

    // M3 steel retention holes
    for (a = [0,120,240]) {
      rotate([0,0,a])
        translate([40, 0, -0.1])
          cylinder(h=rotor_thickness+0.2, d=m3_clear);
    }

    // elephant-foot chamfer on build-plate rim
    translate([0,0,-0.01])
      difference() {
        cylinder(h=elephant_foot, d=rotor_od+0.2);
        cylinder(h=elephant_foot+0.02, d=rotor_od - 1.2);
      }
  }
}
