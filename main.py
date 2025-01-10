import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QFileDialog, QToolBar, QAction
from canvas import Canvas
from file_operations import import_svg, convert_png_to_svg, export_dxf
from ui import UI


class CADApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('House CAD Software')
        self.setGeometry(100, 100, 1000, 800)

        self.canvas = Canvas(self)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        import_svg_button = QPushButton('Import SVG', self)
        import_svg_button.clicked.connect(self.import_svg)
        layout.addWidget(import_svg_button)

        import_png_button = QPushButton('Convert PNG to SVG', self)
        import_png_button.clicked.connect(self.convert_png_to_svg)
        layout.addWidget(import_png_button)

        export_dxf_button = QPushButton('Export as DXF', self)
        export_dxf_button.clicked.connect(self.export_dxf)
        layout.addWidget(export_dxf_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.add_toolbar_actions()

    def add_toolbar_actions(self):
        zoom_in_action = QAction('Zoom In', self)
        zoom_in_action.triggered.connect(self.canvas.zoom_in)
        self.toolbar.addAction(zoom_in_action)

        zoom_out_action = QAction('Zoom Out', self)
        zoom_out_action.triggered.connect(self.canvas.zoom_out)
        self.toolbar.addAction(zoom_out_action)

        reset_view_action = QAction('Reset View', self)
        reset_view_action.triggered.connect(self.canvas.reset_view)
        self.toolbar.addAction(reset_view_action)

    def import_svg(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Import SVG', '', 'SVG Files (*.svg)')
        if file_path:
            self.canvas.import_svg(file_path)

    def convert_png_to_svg(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Convert PNG to SVG', '', 'Image Files (*.png *.jpg *.jpeg)')
        if file_path:
            self.canvas.png_to_svg(file_path)

    def export_dxf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Export as DXF', '', 'DXF Files (*.dxf)')
        if file_path:
            self.canvas.export_dxf(file_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CADApp()
    window.show()
    app.exec_()
