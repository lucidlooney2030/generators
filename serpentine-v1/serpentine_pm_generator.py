"""serpentine_pm_generator.py
Dual-magnet serpentine-coil generator, v1.
16x outer N52 Ø20x5 mm, 48x inner N52 ×5x5 mm (groups of 3).
Serpentine coil former with through-holes for weaving.
"""
import cadquery as cq

# ---- Parameters ----
OM_D, OM_T = 20.0, 5.0
OM_POCKET_D, OM_POCKET_DEPTH = 20.40, 5.35
N_OUTER = 16

IM_D, IM_T = 5.0, 5.0
IM_POCKET_D, IM_POCKET_DEPTH = 5.40, 5.35
N_INNER_GROUPS, GROUP_SIZE = 16, 3

CF_HOLE_D, CF_ROWS, CF_COLS = 2.5, 5, 32

def outer_rotor():
    r = OM_D * N_OUTER * 0.30
    body = cq.Workplane("XY").circle(OM_D*N_OUTER*0.31).extrude(OM_T+2)
    for i in range(N_OUTER):
        a = i*360/N_OUTER
        body = body.faces(">Z").workplane().center(r*cq.exporters.math.cos(a), r*cq.exporters.math.sin(a)).hole(OM_POCKET_D, OM_POCKET_DEPTH)
    return body

def inner_hub():
    r = IM_D * N_INNER_GROUPS * 0.26
    body = cq.Workplane("XY").circle(IM_D*N_INNER_GROUPS*0.28).extrude(IM_T*GROUP_SIZE+2)
    for i in range(N_INNER_GROUPS):
        a = i*360/N_INNER_GROUPS
        for g in range(GROUP_SIZE):
            body = (body.faces(">Z").workplane(offset=1+g*IM_T)
                    .center(r*cq.exporters.math.cos(a), r*cq.exporters.math.sin(a))
                    .hole(IM_POCKET_D, IM_POCKET_DEPTH))
    return body

def coil_former():
    r = OM_D * N_OUTER * 0.30
    body = cq.Workplane("XY").circle(OM_D*N_OUTER*0.31).extrude(CF_ROWS*4)
    for c in range(CF_COLS):
        a = c*360/CF_COLS
        for row in range(CF_ROWS):
            body = (body.faces(">Z").workplane(offset=2+row*4)
                    .center(r*cq.exporters.math.cos(a), r*cq.exporters.math.sin(a))
                    .hole(CF_HOLE_D, 6))
    return body

def stator_stand():
    body = cq.Workplane("XY").circle(OM_D*N_OUTER*0.35).extrude(10)
    body = body.faces(">Z").hole(22, 12)  # 608 bearing
    for i in range(3):
        a = i*120
        body = body.faces(">Z").workplane().center(OM_D*N_OUTER*0.32*cq.exporters.math.cos(a),
                                                   OM_D*N_OUTER*0.32*cq.exporters.math.sin(a)).hole(8, 12)
    return body

if __name__ == "__main__":
    import os
    os.makedirs("stl", exist_ok=True)
    cq.exporters.export(outer_rotor(), "stl/01_outer_magnet_rotor.stl")
    cq.exporters.export(inner_hub(), "stl/02_inner_magnet_hub.stl")
    cq.exporters.export(coil_former(), "stl/03_serpentine_coil_former.stl")
    cq.exporters.export(stator_stand(), "stl/04_stator_cap_stand.stl")
    print("exported 4 STLs")
