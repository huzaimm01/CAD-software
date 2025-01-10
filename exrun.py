from PyQt5.QtWidgets import QApplication
from canvas import Canvas

if __name__ == "__main__":
    app = QApplication([])
    canvas = Canvas(None)  # Initialize the Canvas widget
    canvas.show()  # Display the widget
    app.exec_()  # Start the application's event loop
