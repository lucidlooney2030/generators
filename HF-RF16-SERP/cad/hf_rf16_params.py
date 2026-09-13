"""HF-RF16-SERP 16P/16S — locked parameters (mm). Radial-flux outer-rotor."""
import math

MAG_COUNT = 16
PITCH_DEG = 360.0 / MAG_COUNT  # 22.5

# Magnets
MAG_DIA = 20.00
MAG_THK = 5.00
MAG_FACE_R = 56.38
MAG_BACK_R = MAG_FACE_R + MAG_THK  # 61.38
AIR_GAP = 1.00

# Sleeve
SLEEVE_OUTER_R = MAG_FACE_R - AIR_GAP  # 55.38
SLEEVE_WALL = 0.80
SLEEVE_INNER_R = SLEEVE_OUTER_R - SLEEVE_WALL  # 54.58
SLEEVE_AXIAL = 22.00

# ---------------------------------------------------------------------------
# GEOMETRY CONFLICT RESOLUTION (see README)
# Original: bore r=47.00, groove floor r=47.38 → wall only 0.38 mm (impossible).
# Preferred: magnet face 56.38, air gap 1.00, sleeve outer 55.38 / wall 0.80.
# Set bore RADIUS = 47.00 (diameter 94.00), wall ≥2.00 → groove floor r = 49.00.
# Copper fill = 55.38 - 0.80 - 49.00 = 5.58 mm.
# Steel tube OD ≈ 94 mm (matches Ø94 bore); legacy BOM "OD~47" was the radius figure.
# ---------------------------------------------------------------------------
BORE_R = 47.00
BORE_D = 2.0 * BORE_R  # 94.00
MIN_PRINTED_WALL = 2.00
GROOVE_FLOOR_R = 49.00  # BORE_R + MIN_PRINTED_WALL
PRINTED_WALL = GROOVE_FLOOR_R - BORE_R  # 2.00
COPPER_FILL = SLEEVE_INNER_R - GROOVE_FLOOR_R  # 5.58
GROOVE_OUTER_R = SLEEVE_OUTER_R  # 55.38
STEEL_TUBE_OD = BORE_D  # ~94
STEEL_TUBE_WALL = 3.00
STEEL_TUBE_LEN = 28.00

# Groove / land at outer radius (arc lengths). Pitch arc = 2*pi*55.38/16 ≈ 21.7505
GROOVE_W = 12.00
LAND_W = 9.75  # 12.00 + 9.75 = 21.75 ✓ at r=55.38
GROOVE_ANGLE_DEG = math.degrees(GROOVE_W / GROOVE_OUTER_R)  # ~12.415°
LAND_ANGLE_DEG = PITCH_DEG - GROOVE_ANGLE_DEG  # ~10.085°

GROOVE_AXIAL = 20.00
GALLERY_AXIAL = 6.00
GALLERY_DEPTH = 4.00
RETURN_SLOT_CIRC = 4.00
RETURN_SLOT_RAD = 3.00
GROOVE_FLOOR_CORNER_R = 3.00
STATOR_AXIAL = GROOVE_AXIAL + 2 * GALLERY_AXIAL  # 32.00
STATOR_BOLT_CIRCLE = 56.00  # diameter
STATOR_M3_PILOT = 2.50

# Rotor
ROTOR_OD = 132.00
ROTOR_OR = ROTOR_OD / 2.0  # 66.00
POCKET_DIA = 20.30
POCKET_DEPTH = 5.20
POCKET_LEAD = 0.40
LIP_THK = 0.80
LIP_ID = 18.40
POCKET_CL_FROM_FLOOR = 12.00
BACKIRON_R_IN = 61.38
BACKIRON_R_OUT = 62.88
BACKIRON_AXIAL = 20.20
STEEL_STRIP = (1.50, 20.00, 386)  # thk, width, cut length
ROTOR_FLOOR = 4.00
ROTOR_INTERIOR_H = 25.00
ROTOR_CUP_H = 29.00  # excl boss = floor + interior
AXIAL_LIP = 2.50
BEARING_BORE = 22.20
BEARING_DEPTH = 7.20
BEARING_FILLET = 1.00
M3_CLR = 3.20
M3_BOLT_CIRCLE = 40.00  # diameter
N_M3_ROTOR = 6
SHAFT_D = 8.00

# Cap
CAP_THK = 3.00
GROMMET_D = 4.00
CAP_BOLT_CIRCLE = 56.00

FILLET_MAJOR = 1.00
EDGE_ROUND = 0.30

def summary():
    return {
        "MAG_COUNT": MAG_COUNT,
        "PITCH_DEG": PITCH_DEG,
        "MAG_FACE_R": MAG_FACE_R,
        "MAG_BACK_R": MAG_BACK_R,
        "AIR_GAP": AIR_GAP,
        "SLEEVE_OUTER_R": SLEEVE_OUTER_R,
        "SLEEVE_INNER_R": round(SLEEVE_INNER_R, 3),
        "BORE_D": BORE_D,
        "BORE_R": BORE_R,
        "GROOVE_FLOOR_R": GROOVE_FLOOR_R,
        "PRINTED_WALL": PRINTED_WALL,
        "COPPER_FILL": round(COPPER_FILL, 3),
        "GROOVE_W": GROOVE_W,
        "LAND_W": LAND_W,
        "GROOVE_ANGLE_DEG": round(GROOVE_ANGLE_DEG, 3),
        "LAND_ANGLE_DEG": round(LAND_ANGLE_DEG, 3),
        "ROTOR_OD": ROTOR_OD,
        "STEEL_STRIP_LEN": STEEL_STRIP[2],
        "STEEL_TUBE_OD": STEEL_TUBE_OD,
        "STATOR_AXIAL": STATOR_AXIAL,
    }

if __name__ == "__main__":
    for k, v in summary().items():
        print(f"{k}: {v}")
