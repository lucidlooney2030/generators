include <parameters.scad>

// Print 2–3 of these; stack to set ~2–3 mm mechanical air gap during setup
module spacer_ring() {
  difference() {
    cylinder(h=1.0, d=40);
    translate([0,0,-0.1])
      cylinder(h=1.2, d=stator_id + 2);
  }
}

spacer_ring();
