include <parameters.scad>

module hand_crank() {
  difference() {
    union() {
      cylinder(h=crank_arm_t, d=28);
      translate([0, -crank_arm_w/2, 0])
        cube([crank_arm_len, crank_arm_w, crank_arm_t]);
      translate([crank_arm_len, 0, 0])
        cylinder(h=crank_arm_t, d=22);
    }
    translate([0,0,-0.1])
      cylinder(h=crank_arm_t+0.2, d=shaft_d + clearance_slip);
    translate([0,0,crank_arm_t/2])
      rotate([0,90,0])
        cylinder(h=20, d=m3_tap);
    translate([crank_arm_len, 0, -0.1])
      cylinder(h=crank_arm_t+0.2, d=m4_clear);
  }
}

hand_crank();
