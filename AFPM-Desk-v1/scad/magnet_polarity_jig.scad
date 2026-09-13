include <parameters.scad>

// Helps place magnets with correct alternating polarity on rotor
module magnet_polarity_jig() {
  difference() {
    cylinder(h=4, d=rotor_od + 10);
    translate([0,0,-0.1])
      cylinder(h=4.2, d=rotor_od + 0.4);
  }
  // labeled stubs pointing to even (N) and odd (S) positions
  for (i = [0:magnet_count-1]) {
    angle = i * 360 / magnet_count;
    rotate([0,0,angle])
      translate([rotor_od/2 + 2, -4, 0]) {
        cube([8, 8, 3]);
        // raised letter-like marks: bar=N, cross=S
        translate([2, 3.5, 3]) {
          if (i % 2 == 0)
            cube([4, 1, 0.8]);
          else {
            cube([4, 1, 0.8]);
            translate([1.5, -1.5, 0]) cube([1, 4, 0.8]);
          }
        }
      }
  }
}

magnet_polarity_jig();
