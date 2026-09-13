include <parameters.scad>

module stator_plate() {
  floor_t = stator_thickness - coil_slot_depth; // ~2 mm
  difference() {
    cylinder(h=stator_thickness, d=stator_od);

    translate([0,0,-0.1])
      cylinder(h=stator_thickness+0.2, d=stator_id);

    // coil pockets — cut from top down, leave floor
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 30;
      rotate([0,0,angle])
        translate([coil_pcd/2 - coil_slot_l/2, -coil_slot_w/2, floor_t])
          cube([coil_slot_l, coil_slot_w, coil_slot_depth + 0.2]);
    }

    // wire exit channels
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 30;
      rotate([0,0,angle])
        translate([stator_od/2 - 12, -2, stator_thickness - 2.5])
          cube([16, 4, 3]);
    }

    // M4 pillar holes
    for (a = [0,120,240]) {
      rotate([0,0,a])
        translate([stator_pillar_pcd/2, 0, -0.1])
          cylinder(h=stator_thickness+0.2, d=m4_clear);
    }

    // index notch
    translate([stator_od/2 - 2, 0, -0.1])
      cylinder(h=stator_thickness+0.2, d=3);
  }
}

stator_plate();
