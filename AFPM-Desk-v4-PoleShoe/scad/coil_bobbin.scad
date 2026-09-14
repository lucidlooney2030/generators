include <parameters.scad>
// Permanent thin bobbin that stays in stator. Print 9.
// Wind ~180–220 turns 26–28 AWG then drop into stator_plate pockets.

bw = former_core_w;
bl = former_core_l;
bh = former_wind_h;
flange = former_flange;

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
