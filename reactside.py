from pprint import pprint
from PySide2.QtWidgets import QWidget

# since it is not possible in python an abstract class inheritances from
# ABC and a QWidget (TypeError: metaclass conflict), we make a "Custom"
# abstract class
def Component(base=QWidget):
    class CustomComponent(base):
        def __init__(self, initial_state, layout):
            if type(self) is CustomComponent:
                raise Exception('Component is an abstract class and cannot be '
                                'instantiated directly')
            super().__init__()
            self.state = initial_state
            self.setLayout(layout)
            self.render_()

        def clear(self):
            if self.layout() is not None:
                while self.layout().count():
                    child = self.layout().takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()
                        # child.widget().setParent(None)

        def render_(self):
            raise NotImplementedError('Subclasses must override render_')

        def set_state(self, state: dict):
            self.state = state
            self.clear()
            self.render_()
            self.show()

    return CustomComponent
