include <parameters.scad>
// Couples Ø8 shaft to rotor. Print TWO. Set screw + 4× M3 to rotor.

hub_flange_d = 36;
hub_flange_t = 4;
hub_boss_d = rotor_hub_bore - 0.2;
hub_boss_h = 5;
hub_collar_d = 18;
hub_collar_h = 12;

module shaft_hub() {
  difference() {
    union() {
      cylinder(h=hub_flange_t, d=hub_flange_d);
      translate([0,0,hub_flange_t])
        cylinder(h=hub_boss_h, d=hub_boss_d);
      translate([0,0,-hub_collar_h])
        cylinder(h=hub_collar_h, d=hub_collar_d);
    }
    translate([0,0,-hub_collar_h-0.1])
      cylinder(h=hub_collar_h+hub_flange_t+hub_boss_h+0.2, d=shaft_d + clearance_slip);

    translate([0,0,-hub_collar_h/2])
      rotate([0,90,0])
        cylinder(h=hub_collar_d, d=m3_tap);

    for (a = [0,90,180,270]) {
      rotate([0,0,a])
        translate([10, 0, -0.1])
          cylinder(h=hub_flange_t+0.2, d=m3_clear);
    }
  }
}

shaft_hub();
