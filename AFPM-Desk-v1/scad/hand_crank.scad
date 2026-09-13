include <parameters.scad>

module hand_crank() {
  difference() {
    union() {
      // hub
      cylinder(h=crank_arm_t, d=24);
      // arm
      translate([0, -crank_arm_w/2, 0])
        cube([crank_arm_len, crank_arm_w, crank_arm_t]);
      // handle boss
      translate([crank_arm_len, 0, 0])
        cylinder(h=crank_arm_t, d=18);
    }
    // shaft bore
    translate([0,0,-0.1])
      cylinder(h=crank_arm_t+0.2, d=shaft_d + 0.15);
    // M3 set screw
    translate([0,0,crank_arm_t/2])
      rotate([90,0,0])
        cylinder(h=20, d=3.2);
    // handle axle hole
    translate([crank_arm_len, 0, -0.1])
      cylinder(h=crank_arm_t+0.2, d=5.2);
  }
}

hand_crank();
