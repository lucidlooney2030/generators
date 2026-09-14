include <parameters.scad>

module stator_plate() {
  floor_t = stator_thickness - coil_slot_depth; // ~2 mm
  difference() {
    cylinder(h=stator_thickness, d=stator_od);

    translate([0,0,-0.1])
      cylinder(h=stator_thickness+0.2, d=stator_id);

    // coil pockets — 9 coils @ 40°; offset 20° vs magnet 0° for AFPM phase
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 20;
      rotate([0,0,angle])
        translate([coil_pcd/2 - coil_slot_l/2, -coil_slot_w/2, floor_t])
          cube([coil_slot_l, coil_slot_w, coil_slot_depth + 0.2]);
    }

    // wire exit channels
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 20;
      rotate([0,0,angle])
        translate([stator_od/2 - 14, -2, stator_thickness - 2.5])
          cube([18, 4, 3]);
    }

    // M4 pillar holes
    for (a = [0,120,240]) {
      rotate([0,0,a])
        translate([stator_pillar_pcd/2, 0, -0.1])
          cylinder(h=stator_thickness+0.2, d=m4_clear);
    }

    // phase labels as shallow notches (A=0, B=1, C=2 pattern)
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 20;
      rotate([0,0,angle])
        translate([stator_od/2 - 3, 0, -0.1])
          cylinder(h=1.2, d=2 + (i % 3)*0.4);
    }

    // index notch
    translate([stator_od/2 - 2, 0, -0.1])
      cylinder(h=stator_thickness+0.2, d=3);
  }
}

stator_plate();
