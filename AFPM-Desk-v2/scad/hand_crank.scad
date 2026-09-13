include <parameters.scad>

module hand_crank() {
  difference() {
    union() {
      // hub
      cylinder(h=crank_arm_t, d=28);
      // arm
      translate([0, -crank_arm_w/2, 0])
        cube([crank_arm_len, crank_arm_w, crank_arm_t]);
      // handle boss
      translate([crank_arm_len, 0, 0])
        cylinder(h=crank_arm_t, d=22);
    }
    // shaft bore
    translate([0,0,-0.1])
      cylinder(h=crank_arm_t+0.2, d=shaft_d + clearance_slip);
    // M3 set screw
    translate([0,0,crank_arm_t/2])
      rotate([0,90,0])
        cylinder(h=20, d=m3_tap);
    // handle pin hole (M4 or printed pin)
    translate([crank_arm_len, 0, -0.1])
      cylinder(h=crank_arm_t+0.2, d=m4_clear);
  }
}

hand_crank();
