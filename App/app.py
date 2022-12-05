from .window import Window
from .frame import Main
class App:
    def __init__(self):
        self.window = Window()
        self.main = Main(self.window)

    def run(self):
        self.window.update()