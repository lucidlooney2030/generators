include <parameters.scad>
// Split bobbin for ~200 turns 28 AWG. Kerf allows removal after winding.

kerf = 0.4;

module coil_former() {
  difference() {
    union() {
      // bottom flange
      translate([0,0,0])
        cube([former_core_l + 2*former_flange, former_core_w + 2*former_flange, 2], center=false);
      // core
      translate([former_flange, former_flange, 2])
        cube([former_core_l, former_core_w, former_wind_h]);
      // top flange
      translate([0,0,2+former_wind_h])
        cube([former_core_l + 2*former_flange, former_core_w + 2*former_flange, 2], center=false);
    }
    // split kerf through middle (lengthwise)
    translate([(former_core_l + 2*former_flange)/2 - kerf/2, -0.1, -0.1])
      cube([kerf, former_core_w + 2*former_flange + 0.2, former_wind_h + 4.2]);
    // lead notch
    translate([-0.1, (former_core_w + 2*former_flange)/2 - 1.5, 2+former_wind_h])
      cube([3, 3, 2.2]);
  }
}

coil_former();
