from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QWidget


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('House CAD Software')
        self.setGeometry(100, 100, 1000, 800)

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
