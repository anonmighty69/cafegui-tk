from tkinter import Toplevel, Button, Label
from .State import get_center
from .Colors import BLUE
class UIFull(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry(get_center(self, 200, 100))
        self.grab_set()

        Label(self, text="Cafe penuh!").grid(row=0, column=0)
        Button(self, text="Kembali", bg=BLUE, width=20, command=lambda: self.destroy()).grid(row=1, column=0, pady=(0, 10))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
