from PyQt5.QtWidgets import QWidget, QInputDialog, QLineEdit, QComboBox, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QRect
from extrusion import extrude_rectangle, extrude_polygon, extrude_stairs
from file_operations import import_svg_file, convert_png_to_svg_file, export_dxf_file


class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StaticContents)
        self.shapes = []
        self.sketches = []  # Store reusable sketches (e.g., stairs)
        self.zoom_factor = 1.0
        self.view_center = (500, 400)
        self.setFixedSize(1000, 800)

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Add buttons for selecting shapes and preset sketches
        self.select_shape_button = QPushButton("Select Shape")
        self.select_shape_button.clicked.connect(self.select_shape)
        self.layout.addWidget(self.select_shape_button)

        self.setLayout(self.layout)

    def select_shape(self):
        # Ask the user which shape to add
        shape_options = ["Rectangle", "Triangle", "Circle", "Polygon", "Stairs"]
        shape, ok = QInputDialog.getItem(self, "Select Shape", "Choose a shape", shape_options, 0, False)

        if ok:
            if shape == "Rectangle":
                self.add_rectangle()
            elif shape == "Triangle":
                self.add_triangle()
            elif shape == "Circle":
                self.add_circle()
            elif shape == "Polygon":
                self.add_polygon()
            elif shape == "Stairs":
                self.add_stairs()

    def add_rectangle(self):
        # Predefined rectangle dimensions
        self.draw_shape(50, 50, 200, 100)

    def add_triangle(self):
        # Predefined triangle dimensions
        self.draw_shape(50, 50, 200, 100)

    def add_circle(self):
        # Predefined circle dimensions
        self.draw_shape(50, 50, 100, 100)

    def add_polygon(self):
        # Ask the user how many sides for the polygon
        num_sides, ok = QInputDialog.getInt(self, "Polygon Sides", "Enter number of sides", 3, 3, 20, 1)

        if ok:
            self.draw_polygon(num_sides)

    def draw_polygon(self, num_sides):
        # Create a polygon with specified number of sides (simplified logic for illustration)
        radius = 100  # Example fixed radius for polygon
        points = []
        angle = 360 / num_sides

        for i in range(num_sides):
            x = 500 + radius * Qt.cos(i * angle * Qt.pi / 180)
            y = 400 + radius * Qt.sin(i * angle * Qt.pi / 180)
            points.append((x, y))

        # Draw polygon (here we use a simplified method, you can refine this logic)
        self.shapes.append(points)
        self.update()

    def add_stairs(self):
        # Predefined stair parameters (can be customized)
        stair_width = 200
        stair_height = 30
        num_steps = 10

        self.sketches.append({
            "type": "stairs",
            "width": stair_width,
            "height": stair_height,
            "num_steps": num_steps
        })
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # Apply zoom and pan transformations
        for shape in self.shapes:
            painter.drawPolygon(*shape)  # Draw custom polygons

        for sketch in self.sketches:
            if sketch["type"] == "stairs":
                # Draw the stairs (this is where extrusion logic comes in)
                self.draw_stairs(painter, sketch)

    def draw_stairs(self, painter, sketch):
        # Draw the stairs with proper spacing between steps
        step_width = sketch["width"]
        step_height = sketch["height"]
        num_steps = sketch["num_steps"]

        for i in range(num_steps):
            step_rect = QRect(500, 400 + i * step_height, step_width, step_height)
            painter.drawRect(step_rect)

    def extrude_selected_shape(self):
        # Use the extrude logic (e.g., rectangle, polygon, stairs)
        selected_shape = self.shapes[-1]  # Just take the last shape for extrusion

        if isinstance(selected_shape, QRect):  # If rectangle
            extrude_rectangle(selected_shape.width(), selected_shape.height(), 100)  # Example depth
        else:
            # Handle other shape types like polygon or stairs
            pass

    def export_dxf(self, file_path):
        # Export the current shapes to a DXF file
        export_dxf_file(self.shapes, file_path)
