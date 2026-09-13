include <parameters.scad>
// Permanent thin bobbin that stays in stator (optional vs free coils).
// Print 6. Wind then drop into stator_plate pockets.

bw = former_core_w + 1;
bl = former_core_l + 1;
bh = coil_slot_depth - 0.4;
flange = 2.5;

module coil_bobbin() {
  difference() {
    union() {
      translate([0,0,0])
        cube([bl + 2*flange, bw + 2*flange, 1.2], center=true);
      translate([0,0,bh/2])
        cube([bl, bw, bh], center=true);
      translate([0,0,bh])
        cube([bl + 2*flange, bw + 2*flange, 1.2], center=true);
    }
    // hollow wind window
    translate([0,0,bh/2])
      cube([bl - 2.4, bw - 2.4, bh + 0.2], center=true);
    // lead slot
    translate([bl/2 + flange/2, 0, bh])
      cube([flange+1, 3, 1.5], center=true);
  }
}

coil_bobbin();
