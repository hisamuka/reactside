import sys
from PySide2.QtWidgets import *

class NicePanel(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel(f"Name: ---")
        self.description = QLabel(f"--- is a such nice guy!!! =D")
        self.label_line_edit = QLabel("Type a new name: ")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.on_click)

        grid = QGridLayout(self)
        grid.addWidget(self.title, 0, 0)
        grid.addWidget(self.description, 1, 0)
        grid.addWidget(self.label_line_edit, 2, 0)
        grid.addWidget(self.line_edit, 2, 1)
        grid.addWidget(self.button, 3, 0)

    def on_click(self):
        name = self.line_edit.text()
        self.title.setText(f"Name: {name}")
        self.description.setText(f"{name} is a such nice guy!!! =D")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.nice_panel = NicePanel()
        self.setCentralWidget(self.nice_panel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

