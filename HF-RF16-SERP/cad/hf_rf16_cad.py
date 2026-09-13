#!/usr/bin/env python3
"""
HF-RF16-SERP 16P/16S — CadQuery generators
Radial-flux OUTER-ROTOR, single-phase wave winding.
"""
from __future__ import annotations

import math
from pathlib import Path

import cadquery as cq

from hf_rf16_params import (
    AIR_GAP,
    AXIAL_LIP,
    BACKIRON_AXIAL,
    BACKIRON_R_IN,
    BACKIRON_R_OUT,
    BEARING_BORE,
    BEARING_DEPTH,
    BEARING_FILLET,
    BORE_R,
    CAP_BOLT_CIRCLE,
    CAP_THK,
    EDGE_ROUND,
    FILLET_MAJOR,
    GALLERY_AXIAL,
    GALLERY_DEPTH,
    GROMMET_D,
    GROOVE_ANGLE_DEG,
    GROOVE_AXIAL,
    GROOVE_FLOOR_CORNER_R,
    GROOVE_FLOOR_R,
    GROOVE_OUTER_R,
    GROOVE_W,
    LAND_W,
    LIP_ID,
    LIP_THK,
    M3_BOLT_CIRCLE,
    M3_CLR,
    MAG_BACK_R,
    MAG_COUNT,
    MAG_DIA,
    MAG_FACE_R,
    MAG_THK,
    N_M3_ROTOR,
    PITCH_DEG,
    POCKET_CL_FROM_FLOOR,
    POCKET_DEPTH,
    POCKET_DIA,
    POCKET_LEAD,
    RETURN_SLOT_CIRC,
    RETURN_SLOT_RAD,
    ROTOR_CUP_H,
    ROTOR_FLOOR,
    ROTOR_INTERIOR_H,
    ROTOR_OD,
    ROTOR_OR,
    SHAFT_D,
    SLEEVE_AXIAL,
    SLEEVE_INNER_R,
    SLEEVE_OUTER_R,
    SLEEVE_WALL,
    STATOR_AXIAL,
    STATOR_BOLT_CIRCLE,
    STATOR_M3_PILOT,
)

OUT = Path(__file__).resolve().parent


def _export_stl(workplane, path: Path, tol: float = 0.1):
    cq.exporters.export(workplane, str(path), exportType="STL", tolerance=tol, angularTolerance=0.2)
    print(f"  STL  {path.name}  ({path.stat().st_size // 1024} KiB)")


def _export_step(obj, path: Path):
    cq.exporters.export(obj, str(path), exportType="STEP")
    print(f"  STEP {path.name}  ({path.stat().st_size // 1024} KiB)")


# ---------------------------------------------------------------------------
# ROTOR
# ---------------------------------------------------------------------------
def make_rotor() -> cq.Workplane:
    """
    Outer-rotor cup. Z=0 at exterior floor face.
    Interior floor at Z=ROTOR_FLOOR. Rim at Z=ROTOR_CUP_H.
    Bearing boss extends below Z=0.
    """
    # Main cup OD solid
    cup = (
        cq.Workplane("XY")
        .circle(ROTOR_OR)
        .extrude(ROTOR_CUP_H)
    )

    # Hollow interior: from Z=ROTOR_FLOOR to Z=ROTOR_CUP_H, ID leaves wall
    # Inner cylindrical wall before pockets ≈ MAG_FACE_R - LIP_THK = 55.58
    # (lip sits at magnet face plane)
    inner_wall_r = MAG_FACE_R - LIP_THK  # 55.58 — free ID of cup
    cup = (
        cup.faces(">Z").workplane()
        .circle(inner_wall_r)
        .cutBlind(-(ROTOR_INTERIOR_H))
    )

    # Back-iron groove: annular cut from BACKIRON_R_IN to BACKIRON_R_OUT
    # Axial: magnet band centered — pocket CL at POCKET_CL_FROM_FLOOR from interior floor
    # Interior floor Z = ROTOR_FLOOR. Pocket CL Z = ROTOR_FLOOR + POCKET_CL_FROM_FLOOR
    z_pocket_cl = ROTOR_FLOOR + POCKET_CL_FROM_FLOOR
    z_bi0 = z_pocket_cl - BACKIRON_AXIAL / 2.0
    z_bi1 = z_pocket_cl + BACKIRON_AXIAL / 2.0
    # Cut annular groove from the OUTSIDE? Spec: continuous groove for steel strip
    # between r=61.38 and 62.88 — accessed how? Typically cut from top or as
    # an internal annular channel. For a printed cup with outer wall, the strip
    # slides into a circumferential slot open at one end or printed as a recess
    # on the inner side of the outer wall behind the magnets.
    # Behind magnets: magnet back at 61.38. Groove r=61.38 to 62.88 is OUTBOARD
    # of magnet backs — inside the printed wall. Open axially from above for insert.
    bi_ring = (
        cq.Workplane("XY")
        .circle(BACKIRON_R_OUT)
        .circle(BACKIRON_R_IN)
        .extrude(BACKIRON_AXIAL)
        .translate((0, 0, z_bi0))
    )
    cup = cup.cut(bi_ring)

    # Magnet pockets on INNER wall — 16×
    # Pocket: cylinder ØPOCKET_DIA, depth POCKET_DEPTH radially outward from
    # the lip aperture plane at r ≈ MAG_FACE_R - small.
    # Construction: for each angle, cut a cylinder whose axis is radial in XY,
    # centered at Z=z_pocket_cl, starting from r = MAG_FACE_R - LIP_THK.
    #
    # Better approach: create pocket as a disc-shaped void:
    # - At magnet face (r=MAG_FACE_R): aperture transitions via lead-in
    # - Lip: from r=MAG_FACE_R-LIP_THK to MAG_FACE_R, hole ØLIP_ID
    # - Main pocket: from r=MAG_FACE_R to MAG_FACE_R+POCKET_DEPTH, hole ØPOCKET_DIA
    #
    # CadQuery radial pocket: use a cylinder along X, then rotate around Z.

    for i in range(MAG_COUNT):
        ang = i * PITCH_DEG
        pocket = _magnet_pocket_solid(z_pocket_cl)
        pocket = pocket.rotate((0, 0, 0), (0, 0, 1), ang)
        cup = cup.cut(pocket)

    # Bearing boss below floor
    boss_extra = BEARING_DEPTH - ROTOR_FLOOR  # protrudes below if >0
    if boss_extra < 0:
        boss_extra = 0
    boss_od = BEARING_BORE + 2 * 4.0  # ~30 mm boss OD
    boss = (
        cq.Workplane("XY")
        .circle(boss_od / 2.0)
        .extrude(BEARING_DEPTH)
        .translate((0, 0, -(boss_extra)))
    )
    # Merge boss with cup (boss overlaps floor region)
    cup = cup.union(boss)

    # Bearing bore
    bore = (
        cq.Workplane("XY")
        .circle(BEARING_BORE / 2.0)
        .extrude(BEARING_DEPTH + 1)
        .translate((0, 0, -(boss_extra)))
    )
    cup = cup.cut(bore)

    # Shaft clearance through (slightly larger than shaft, smaller than bearing ID)
    # 608ZZ ID = 8.00; leave floor with bearing only — shaft passes through bearing.
    # Add small through-hole for shaft if boss doesn't already clear:
    # Bearing bore is enough.

    # 6× M3 clearance on 40 mm circle, through floor+boss
    for i in range(N_M3_ROTOR):
        a = i * (360.0 / N_M3_ROTOR)
        x = (M3_BOLT_CIRCLE / 2.0) * math.cos(math.radians(a))
        y = (M3_BOLT_CIRCLE / 2.0) * math.sin(math.radians(a))
        hole = (
            cq.Workplane("XY")
            .center(x, y)
            .circle(M3_CLR / 2.0)
            .extrude(BEARING_DEPTH + ROTOR_FLOOR + 2)
            .translate((0, 0, -(boss_extra) - 1))
        )
        cup = cup.cut(hole)

    # Fillets on major transitions — selective to avoid kernel failures
    try:
        cup = cup.edges("%Circle").edges(cq.selectors.RadiusNthSelector(0)).fillet(0.5)
    except Exception:
        pass
    try:
        # Exterior bottom edge of cup OD
        cup = cup.edges("<Z").fillet(EDGE_ROUND)
    except Exception:
        pass

    return cup


def _magnet_pocket_solid(z_cl: float) -> cq.Workplane:
    """
    Single magnet pocket aligned along +X (radial), centered at Z=z_cl.
    Cut volume includes lip bore + main pocket + 0.4×45° lead-in.
    """
    # Main pocket cylinder: axis along X, from r=MAG_FACE_R - LIP_THK - 0.5
    # to r=MAG_FACE_R + POCKET_DEPTH
    r0 = MAG_FACE_R - LIP_THK - 0.5  # start slightly inside cup ID
    r1 = MAG_FACE_R + POCKET_DEPTH  # pocket floor

    # Wide pocket body (ØPOCKET_DIA) for magnet
    body = (
        cq.Workplane("YZ")
        .workplane(offset=MAG_FACE_R - 0.05)
        .circle(POCKET_DIA / 2.0)
        .extrude(POCKET_DEPTH + 0.05)
    )
    # Shift so cylinder axis is at Z=z_cl (Workplane YZ is at x=offset, origin y=0,z=0)
    body = body.translate((0, 0, z_cl))

    # Lip aperture (ØLIP_ID) from inner wall through lip thickness
    lip = (
        cq.Workplane("YZ")
        .workplane(offset=MAG_FACE_R - LIP_THK - 0.5)
        .circle(LIP_ID / 2.0)
        .extrude(LIP_THK + 0.55)
        .translate((0, 0, z_cl))
    )

    # Lead-in: 0.4×45° chamfer at pocket entrance (magnet face plane)
    # Approximate as a short cone / larger cylinder at entrance
    lead_r = POCKET_DIA / 2.0 + POCKET_LEAD
    lead = (
        cq.Workplane("YZ")
        .workplane(offset=MAG_FACE_R - POCKET_LEAD)
        .circle(lead_r)
        .workplane(offset=POCKET_LEAD)
        .circle(POCKET_DIA / 2.0)
        .loft()
        .translate((0, 0, z_cl))
    )

    return body.union(lip).union(lead)


# ---------------------------------------------------------------------------
# STATOR
# ---------------------------------------------------------------------------
def make_stator() -> cq.Workplane:
    """
    Grooved stator drum. Z=0 at bottom end face.
    Grooves open outward. Bore for steel tube.
    """
    outer_r = GROOVE_OUTER_R
    axial = STATOR_AXIAL

    drum = cq.Workplane("XY").circle(outer_r).extrude(axial)

    # Inner bore
    drum = (
        drum.faces(">Z").workplane()
        .circle(BORE_R)
        .cutBlind(-axial)
    )

    # Groove axial band centered
    z0 = GALLERY_AXIAL
    z1 = GALLERY_AXIAL + GROOVE_AXIAL

    # Cut 16 axial grooves
    for i in range(MAG_COUNT):
        ang = i * PITCH_DEG
        groove = _axial_groove_cut(z0, z1)
        groove = groove.rotate((0, 0, 0), (0, 0, 1), ang)
        drum = drum.cut(groove)

    # End-turn galleries: 4 mm deep from outer, 6 mm axial, connecting adjacent
    # TOP (Z near axial): connect odd→even (groove i to i+1 for odd i)
    # BOTTOM: connect even→odd
    # Spec: "odd–even TOP, even–odd BOTTOM" for meander up1, over, down2, ...
    # So at TOP: galleries between grooves 1-2, 3-4, 5-6, ... (0-indexed: 0-1, 2-3, ...)
    # At BOTTOM: galleries between 2-3, 4-5, ... (0-indexed: 1-2, 3-4, ...)
    # Plus wrap-around as needed.

    for i in range(0, MAG_COUNT, 2):
        # TOP galleries between i and i+1
        gal = _gallery_cut(i, i + 1, z_start=z1, z_end=axial)
        drum = drum.cut(gal)
    for i in range(1, MAG_COUNT, 2):
        # BOTTOM galleries between i and (i+1)%16
        gal = _gallery_cut(i, (i + 1) % MAG_COUNT, z_start=0, z_end=GALLERY_AXIAL)
        drum = drum.cut(gal)

    # Circumferential return slot groove16→groove1 (index 15→0) at start axial end
    # 4.00×3.00 — place at bottom end connecting 15 to 0 (in addition to gallery pattern)
    # Spec: after 16 grooves wave ends at start axial end; return for multi-turn
    ret = _return_slot_cut()
    drum = drum.cut(ret)

    # M3 pilot bosses each end face on 56 mm circle — 2 per end
    # Bosses as raised pads with Ø2.5 pilots
    for end_z, sign in ((0.0, -1), (axial, +1)):
        for j, a0 in enumerate((0.0, 180.0)):
            ang = a0 + (0 if end_z == 0 else 90)  # stagger ends optional; use 0 & 180 both ends
            # Spec: two M3 each end on 56 mm circle — angles 0° and 180° both ends is fine
            # but then bolts align — use 0°/180° bottom, 90°/270° top for 4 distinct
            if end_z > 0:
                ang = 90.0 + j * 180.0
            else:
                ang = 0.0 + j * 180.0
            x = (STATOR_BOLT_CIRCLE / 2.0) * math.cos(math.radians(ang))
            y = (STATOR_BOLT_CIRCLE / 2.0) * math.sin(math.radians(ang))
            # Raised boss 3 mm
            boss_h = 3.0
            boss_r = 4.0
            if sign < 0:
                boss = (
                    cq.Workplane("XY")
                    .center(x, y)
                    .circle(boss_r)
                    .extrude(boss_h)
                    .translate((0, 0, -boss_h))
                )
                pilot = (
                    cq.Workplane("XY")
                    .center(x, y)
                    .circle(STATOR_M3_PILOT / 2.0)
                    .extrude(boss_h + 2)
                    .translate((0, 0, -boss_h - 0.5))
                )
            else:
                boss = (
                    cq.Workplane("XY")
                    .center(x, y)
                    .circle(boss_r)
                    .extrude(boss_h)
                    .translate((0, 0, axial))
                )
                pilot = (
                    cq.Workplane("XY")
                    .center(x, y)
                    .circle(STATOR_M3_PILOT / 2.0)
                    .extrude(boss_h + 2)
                    .translate((0, 0, axial - 0.5))
                )
            drum = drum.union(boss).cut(pilot)

    return drum


def _axial_groove_cut(z0: float, z1: float) -> cq.Workplane:
    """
    One open-outward axial groove centered on +X.
    Width GROOVE_W (arc) at outer; floor at GROOVE_FLOOR_R with corner radii.
    """
    # Use a rectangular-ish radial cut with rounded floor.
    # Half-angle for groove:
    half_ang = GROOVE_ANGLE_DEG / 2.0
    # Build as extruded 2D profile in XY then extrude Z — actually cut a sector wedge
    # from GROOVE_FLOOR_R to outer+margin, spanning groove angle, then round floor corners.

    # Simpler robust approach: box cut from floor to outside, width = chord at mid-radius
    mid_r = 0.5 * (GROOVE_FLOOR_R + GROOVE_OUTER_R)
    # Chord width at outer for angular span:
    half_w = GROOVE_OUTER_R * math.sin(math.radians(half_ang))
    # Radial depth
    depth = GROOVE_OUTER_R - GROOVE_FLOOR_R + 0.5  # slight overcut past outer

    # Box centered on +X, extending from x=GROOVE_FLOOR_R to x=GROOVE_OUTER_R+0.5
    # Width 2*half_w along Y, height (z1-z0) along Z
    box = (
        cq.Workplane("XY")
        .center(GROOVE_FLOOR_R + depth / 2.0, 0)
        .box(depth, 2 * half_w, z1 - z0)
        .translate((0, 0, (z0 + z1) / 2.0))
    )

    # Floor corner relief: two cylinders along Z at floor corners (optional aesthetic)
    # Spec: 3.00 mm corner radius at groove floor — approximate with cylindrical blends
    # Cut extra rounded trough at floor using a cylinder of r=GROOVE_FLOOR_CORNER_R
    # along the groove, at the floor corners in the YZ sense.
    # For manufacturability, add a cylindrical cut along Z at each groove-floor corner.
    cr = GROOVE_FLOOR_CORNER_R
    # Place cylinder axes at (GROOVE_FLOOR_R + cr, ± half_w_at_floor approx)
    half_w_floor = GROOVE_FLOOR_R * math.sin(math.radians(half_ang))
    for sgn in (-1, 1):
        cyl = (
            cq.Workplane("XY")
            .center(GROOVE_FLOOR_R + cr, sgn * (half_w_floor - 0.1))
            .circle(cr)
            .extrude(z1 - z0)
            .translate((0, 0, z0))
        )
        # Only keep the part that rounds the corner — union with box is enough if we
        # cut both; a full cylinder would overcut lands. Intersect with groove sector.
        # Simpler: skip aggressive corner cyl if it risks land damage; use fillet after.
        box = box.union(cyl)

    return box


def _gallery_cut(i0: int, i1: int, z_start: float, z_end: float) -> cq.Workplane:
    """Circumferential gallery connecting groove i0 to i1 at given Z band."""
    a0 = i0 * PITCH_DEG
    a1 = i1 * PITCH_DEG
    # Mid-angle
    # Handle wrap
    if i1 < i0:
        amid = (a0 + a1 + 360.0) / 2.0
    else:
        amid = (a0 + a1) / 2.0
    amid = amid % 360.0

    # Gallery spans roughly one land between grooves, depth GALLERY_DEPTH from outer
    span_ang = PITCH_DEG  # covers from groove center to next
    # Build arc-slot: box at mid radius bent — approximate with box rotated to amid
    r_inner = GROOVE_OUTER_R - GALLERY_DEPTH
    depth = GALLERY_DEPTH + 0.5
    # Chord length spanning land + half grooves
    half_span = span_ang / 2.0
    half_w = GROOVE_OUTER_R * math.sin(math.radians(half_span))
    h = z_end - z_start

    gal = (
        cq.Workplane("XY")
        .center(r_inner + depth / 2.0, 0)
        .box(depth, 2 * half_w * 0.85, h)
        .translate((0, 0, (z_start + z_end) / 2.0))
        .rotate((0, 0, 0), (0, 0, 1), amid)
    )
    return gal


def _return_slot_cut() -> cq.Workplane:
    """4×3 circumferential return slot from groove 15 to groove 0 at bottom."""
    # Place at bottom Z band, spanning across land between groove 15 and 0 (at angle 0/-11.25)
    amid = (15 * PITCH_DEG + 360.0) / 2.0 % 360.0  # ≈ 348.75? 
    # Centers at 15*22.5=337.5 and 0. Mid = 348.75
    amid = 337.5 + 11.25  # 348.75
    r_inner = GROOVE_OUTER_R - RETURN_SLOT_RAD - 0.5
    depth = RETURN_SLOT_RAD + 1.0
    # Circumferential width 4 mm
    half_w = RETURN_SLOT_CIRC / 2.0
    h = GALLERY_AXIAL  # within bottom gallery zone
    slot = (
        cq.Workplane("XY")
        .center(r_inner + depth / 2.0, 0)
        .box(depth, RETURN_SLOT_CIRC, h)
        .translate((0, 0, h / 2.0))
        .rotate((0, 0, 0), (0, 0, 1), amid)
    )
    return slot


# ---------------------------------------------------------------------------
# SLEEVE (two 180° shells in one compound)
# ---------------------------------------------------------------------------
def make_sleeve() -> cq.Workplane:
    """Two 180° shells, outer r=55.38, wall 0.80, axial 22. Snap clips."""
    h0, h1 = make_sleeve_halves()
    return h0.union(h1)


def make_sleeve_halves() -> tuple[cq.Workplane, cq.Workplane]:
    """Return two separate 180° sleeve shells (outer r=55.38, wall 0.80, axial 22)."""
    full = (
        cq.Workplane("XY")
        .circle(SLEEVE_OUTER_R)
        .circle(SLEEVE_INNER_R)
        .extrude(SLEEVE_AXIAL)
    )
    halves = []
    for a0 in (0.0, 180.0):
        # Keep half-plane via oversized box intersect, then rotate into place
        keep = (
            cq.Workplane("XY")
            .rect(SLEEVE_OUTER_R * 2 + 5, SLEEVE_OUTER_R + 3)
            .extrude(SLEEVE_AXIAL)
            .translate((0, (SLEEVE_OUTER_R + 3) / 2.0, 0))
        )
        shell = full.intersect(keep)
        shell = shell.rotate((0, 0, 0), (0, 0, 1), a0)
        # 3× M2 clip bosses on inner face, centered on the 180° arc
        for az in (-60.0, 0.0, 60.0):
            ang = a0 + 90.0 + az
            cx = (SLEEVE_INNER_R - 0.6) * math.cos(math.radians(ang))
            cy = (SLEEVE_INNER_R - 0.6) * math.sin(math.radians(ang))
            clip = (
                cq.Workplane("XY")
                .center(cx, cy)
                .circle(1.6)
                .extrude(2.0)
                .translate((0, 0, SLEEVE_AXIAL / 2.0 - 1.0))
            )
            hole = (
                cq.Workplane("XY")
                .center(cx, cy)
                .circle(1.1)
                .extrude(3.0)
                .translate((0, 0, SLEEVE_AXIAL / 2.0 - 1.5))
            )
            shell = shell.union(clip).cut(hole)
        halves.append(shell)
    return halves[0], halves[1]


# ---------------------------------------------------------------------------
# CAP
# ---------------------------------------------------------------------------
def make_cap() -> cq.Workplane:
    """
    End cap covering stator. Bearing seat for second 608ZZ.
    4× M3 to stator bosses. Grommet holes. Shaft clearance.
    """
    # Cap plate OD slightly over stator outer
    cap_or = GROOVE_OUTER_R + 3.0  # 58.38
    cap = cq.Workplane("XY").circle(cap_or).extrude(CAP_THK)

    # Bearing boss upward
    boss_od = BEARING_BORE + 8.0
    boss = (
        cq.Workplane("XY")
        .circle(boss_od / 2.0)
        .extrude(BEARING_DEPTH)
    )
    cap = cap.union(boss)

    # Bearing bore
    bore = (
        cq.Workplane("XY")
        .circle(BEARING_BORE / 2.0)
        .extrude(BEARING_DEPTH + 0.5)
    )
    cap = cap.cut(bore)

    # Shaft clearance through plate (bearing ID path)
    # Already cleared by bearing bore through boss; ensure plate is open:
    # bearing bore from Z=0 through boss is enough if plate is within boss footprint.
    # Add through hole in case:
    thru = (
        cq.Workplane("XY")
        .circle(SHAFT_D / 2.0 + 0.3)
        .extrude(CAP_THK + BEARING_DEPTH)
    )
    # Don't cut larger than bearing — shaft goes through bearing.
    # Skip extra cut.

    # 4× M3 clearance on 56 mm circle (match stator bosses at 0/180 bottom + 90/270 top
    # Cap bolts to ONE end — use 0° and 180° plus we need 4 holes: use 0,90,180,270
    for i in range(4):
        a = i * 90.0
        x = (CAP_BOLT_CIRCLE / 2.0) * math.cos(math.radians(a))
        y = (CAP_BOLT_CIRCLE / 2.0) * math.sin(math.radians(a))
        hole = (
            cq.Workplane("XY")
            .center(x, y)
            .circle(M3_CLR / 2.0)
            .extrude(CAP_THK + 1)
            .translate((0, 0, -0.5))
        )
        cap = cap.cut(hole)

    # 2× Ø4 grommet holes for winding tails
    for a in (45.0, 225.0):
        x = 22.0 * math.cos(math.radians(a))
        y = 22.0 * math.sin(math.radians(a))
        g = (
            cq.Workplane("XY")
            .center(x, y)
            .circle(GROMMET_D / 2.0)
            .extrude(CAP_THK + 1)
            .translate((0, 0, -0.5))
        )
        cap = cap.cut(g)

    try:
        cap = cap.edges("|Z").edges(cq.selectors.RadiusNthSelector(0)).fillet(0.5)
    except Exception:
        pass
    try:
        # Fillet at boss base
        cap = cap.edges(cq.Selector("and(>Z, %Circle)")).fillet(BEARING_FILLET)
    except Exception:
        pass

    return cap


# ---------------------------------------------------------------------------
# Assembly helpers (positioned solids for STEP)
# ---------------------------------------------------------------------------
def build_assembly():
    """Return dict of named positioned solids for STEP assembly export."""
    rotor = make_rotor()
    stator = make_stator()
    sleeve = make_sleeve()
    cap = make_cap()

    # Position: stator centered so groove band aligns with magnet band.
    # Rotor: interior floor at Z=0 interior → pocket CL at 12 from interior floor.
    # Stator: groove from GALLERY_AXIAL to GALLERY_AXIAL+GROOVE_AXIAL.
    # Align magnet band center with groove center.
    z_pocket_cl = ROTOR_FLOOR + POCKET_CL_FROM_FLOOR
    z_groove_cl = GALLERY_AXIAL + GROOVE_AXIAL / 2.0
    # Stator shift so groove CL matches pocket CL
    stator_z = z_pocket_cl - z_groove_cl
    stator = stator.translate((0, 0, stator_z))

    # Sleeve centered on groove / magnet band
    sleeve_z = z_pocket_cl - SLEEVE_AXIAL / 2.0
    sleeve = sleeve.translate((0, 0, sleeve_z))

    # Cap on top of stator
    cap_z = stator_z + STATOR_AXIAL
    cap = cap.translate((0, 0, cap_z))

    return {
        "ROTOR": rotor,
        "STATOR": stator,
        "SLEEVE": sleeve,
        "CAP": cap,
    }


def export_all():
    OUT.mkdir(parents=True, exist_ok=True)
    print("Building ROTOR...")
    rotor = make_rotor()
    _export_stl(rotor, OUT / "HF-RF16-ROTOR.stl")
    _export_step(rotor, OUT / "HF-RF16-ROTOR.step")

    print("Building STATOR...")
    stator = make_stator()
    _export_stl(stator, OUT / "HF-RF16-STATOR.stl")
    _export_step(stator, OUT / "HF-RF16-STATOR.step")

    print("Building SLEEVE...")
    sleeve = make_sleeve()
    _export_stl(sleeve, OUT / "HF-RF16-SLEEVE.stl")
    _export_step(sleeve, OUT / "HF-RF16-SLEEVE.step")

    print("Building CAP...")
    cap = make_cap()
    _export_stl(cap, OUT / "HF-RF16-CAP.stl")
    _export_step(cap, OUT / "HF-RF16-CAP.step")

    print("Building ASSEMBLY STEP...")
    parts = build_assembly()
    # Compound all for single STEP
    asm = parts["ROTOR"]
    for name in ("STATOR", "SLEEVE", "CAP"):
        asm = asm.union(parts[name])
    _export_step(asm, OUT / "HF-RF16-ASSEMBLY.step")

    print("Building ONEPLATE...")
    one = _oneplate(rotor, stator, sleeve, cap)
    _export_stl(one, OUT / "HF-RF16-ONEPLATE.stl")

    print("Done.")


def _oneplate(rotor, stator, sleeve, cap) -> cq.Workplane:
    """Arrange parts on one 300 mm bed with 8 mm spacing."""
    gap = 8.0
    # Bounding placements (approximate centers)
    # Rotor ~132 OD, stator ~110 OD, sleeve ~110, cap ~117
    r = rotor
    s = stator.translate((ROTOR_OD / 2 + GROOVE_OUTER_R + gap, 0, 0))
    # Sleeve next
    sl = sleeve.translate((ROTOR_OD / 2 + 2 * GROOVE_OUTER_R + SLEEVE_OUTER_R + 2 * gap, 0, 0))
    # Cap below rotor
    c = cap.translate((0, -(ROTOR_OD / 2 + GROOVE_OUTER_R + 3 + gap), 0))
    return r.union(s).union(sl).union(c)


if __name__ == "__main__":
    export_all()
