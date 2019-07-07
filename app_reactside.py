import sys
from PySide2.QtWidgets import *

from reactside import Component

class NicePanel(Component(QWidget)):
    def __init__(self):
        initial_state = {"name": "---", "age": 10}
        layout = QGridLayout()
        super().__init__(initial_state, layout)

    def render_(self):
        self.title = QLabel(f"Name: {self.state['name']}")
        self.description = QLabel(f"{self.state['name']} is a such nice "
                                  f"guy!!! =D")

        self.label_line_edit = QLabel("Type a new name: ")
        self.line_edit = QLineEdit()
        self.button = QPushButton("Submit")
        self.button.clicked.connect(
            lambda : self.set_state({"name": self.line_edit.text()}))

        grid = self.layout()
        grid.addWidget(self.title, 0, 0)
        grid.addWidget(self.description, 1, 0)
        grid.addWidget(self.label_line_edit, 2, 0)
        grid.addWidget(self.line_edit, 2, 1)
        grid.addWidget(self.button, 3, 0)


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

