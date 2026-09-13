include <parameters.scad>

module stator_mount() {
  difference() {
    union() {
      // stator ring plate
      cylinder(h=stator_thickness, d=stator_od);
      // mounting ears
      for (a = [0, 120, 240]) {
        rotate([0,0,a])
          translate([stator_od/2 - 5, 0, 0])
            cylinder(h=stator_thickness, d=18);
      }
    }
    
    // center clearance for shaft / hub
    translate([0,0,-0.1])
      cylinder(h=stator_thickness+0.2, d=stator_id);
    
    // coil pockets (rectangular-ish with rounded ends)
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 30; // offset vs magnets for continuous EMF
      rotate([0,0,angle])
        translate([coil_pcd/2, 0, stator_thickness - coil_slot_depth]) {
          hull() {
            translate([-coil_slot_h/2 + coil_slot_w/4, 0, 0])
              cylinder(h=coil_slot_depth+0.1, d=coil_slot_w);
            translate([coil_slot_h/2 - coil_slot_w/4, 0, 0])
              cylinder(h=coil_slot_depth+0.1, d=coil_slot_w);
          }
        }
    }
    
    // wire exit channels (radial grooves on bottom face)
    for (i = [0:coil_count-1]) {
      angle = i * 360 / coil_count + 30;
      rotate([0,0,angle])
        translate([stator_id/2 + 2, -1.5, -0.05])
          cube([stator_od/2 - stator_id/2 - 4, 3, 2]);
    }
    
    // ear mounting holes M4
    for (a = [0, 120, 240]) {
      rotate([0,0,a])
        translate([stator_od/2 - 5, 0, -0.1])
          cylinder(h=stator_thickness+0.2, d=4.2);
    }
    
    // phase label pits A B C (tiny)
    for (i = [0:2]) {
      angle = i * 120 + 30;
      rotate([0,0,angle])
        translate([stator_od/2 - 12, 0, stator_thickness - 0.4])
          cylinder(h=0.5, d=3);
    }
  }
}

stator_mount();
