include <parameters.scad>

// Fit coupon: magnet pockets + 608 seat variants for Kobra PETG calibration
module fit_coupon() {
    difference() {
        hull() {
            translate([-35, -18, 0]) cube([70, 36, 8]);
        }
        // Magnet pocket diameter variants: +0.2, +0.25, +0.3
        for (i = [0:2]) {
            d = magnet_d + 0.2 + i * 0.05;
            translate([-22 + i * 22, 6, 8 - (magnet_h + magnet_pocket_z)])
                cylinder(h = magnet_h + magnet_pocket_z + 0.2, d = d);
        }
        // 608 seats: undersize 0.10, 0.15, 0.20 total
        for (i = [0:2]) {
            d = bearing_od - (0.10 + i * 0.05);
            translate([-22 + i * 22, -8, -0.1])
                cylinder(h = 8.2, d = d);
        }
    }
    // Labels as raised bars (count notches)
    for (i = [0:2]) translate([-22 + i * 22 - 1, 16, 8]) cube([2, 1 + i, 0.4]);
}
fit_coupon();
