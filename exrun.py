from PyQt5.QtWidgets import QApplication
from canvas import Canvas

if __name__ == "__main__":
    app = QApplication([])
    canvas = Canvas(None)
    canvas.show() 
    app.exec_() 
