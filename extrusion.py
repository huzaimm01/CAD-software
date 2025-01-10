from OCC.Core.gp import gp_Pnt, gp_Vec
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Display.SimpleGui import init_display


def extrude_rectangle(width=100, height=50, depth=100):
    p1 = gp_Pnt(0, 0, 0)
    p2 = gp_Pnt(width, 0, 0)
    p3 = gp_Pnt(width, height, 0)
    p4 = gp_Pnt(0, height, 0)

    edge1 = BRepBuilderAPI_MakeEdge(p1, p2).Edge()
    edge2 = BRepBuilderAPI_MakeEdge(p2, p3).Edge()
    edge3 = BRepBuilderAPI_MakeEdge(p3, p4).Edge()
    edge4 = BRepBuilderAPI_MakeEdge(p4, p1).Edge()

    wire = BRepBuilderAPI_MakeWire(edge1, edge2, edge3, edge4).Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()
    prism = BRepPrimAPI_MakePrism(face, gp_Vec(0, 0, depth)).Shape()

    display, start_display = init_display()
    display.DisplayShape(prism, update=True)
    start_display()


def extrude_polygon(points, depth=100):
    # Create edges based on points and extrude
    edges = []
    for i in range(len(points)):
        p1 = gp_Pnt(points[i][0], points[i][1], 0)
        p2 = gp_Pnt(points[(i + 1) % len(points)][0], points[(i + 1) % len(points)][1], 0)
        edges.append(BRepBuilderAPI_MakeEdge(p1, p2).Edge())

    wire = BRepBuilderAPI_MakeWire(*edges).Wire()
    face = BRepBuilderAPI_MakeFace(wire).Face()
    prism = BRepPrimAPI_MakePrism(face, gp_Vec(0, 0, depth)).Shape()

    display, start_display = init_display()
    display.DisplayShape(prism, update=True)
    start_display()


def extrude_stairs(width, height, num_steps, step_depth=100):
    # Create stairs by extruding each step
    steps = []
    for i in range(num_steps):
        step = extrude_rectangle(width, height, step_depth)  # You can modify this for each step
        steps.append(step)

    display, start_display = init_display()
    for step in steps:
        display.DisplayShape(step, update=True)
    start_display()
