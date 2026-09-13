include <parameters.scad>

module shaft_hub() {
  difference() {
    union() {
      cylinder(h=12, d=28);
      translate([0,0,12])
        cylinder(h=6, d=rotor_id - 0.2); // press into rotor
    }
    // shaft bore
    translate([0,0,-0.1])
      cylinder(h=20, d=shaft_d + 0.15);
    // M3 set screw hole
    translate([0, 0, 6])
      rotate([90,0,0])
        cylinder(h=20, d=3.2);
    // M3 rotor bolt holes matching rotor_disk
    for (a = [0,90,180,270]) {
      rotate([0,0,a])
        translate([10, 0, -0.1])
          cylinder(h=12.2, d=3.2);
    }
  }
}

shaft_hub();
