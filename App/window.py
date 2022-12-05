from tkinter import Tk, Frame
from .config import TITLE, WIDTH, HEIGHT
from .utils import get_center

class Window(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.config()

    def config(self) -> None:
        self.title(TITLE)
        self.geometry(get_center(self, WIDTH, HEIGHT))
        self.resizable(width=False, height=False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def update(self) -> None:
        self.mainloop()




