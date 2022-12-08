from tkinter import Toplevel, Button, Label
from .State import get_center
from .Colors import BLUE

WIDTH = 200
HEIGHT = 100

# Pop up window untuk meja penuh
class UIFull(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        # konfigurasi window
        self.configWindow(WIDTH, HEIGHT)

        # tampil ui
        self.initUI()

    # Konfigurasi window
    def configWindow(self, w: int, h: int) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.resizable(False, False)
        self.geometry(get_center(self, w, h))
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # Tampil UI
    def initUI(self) -> None:
        labelInfo = Label(self, text="Cafe penuh!")
        labelInfo.grid(row=0, column=0)

        buttonKembali = Button(
            self, 
            text="Kembali", 
            bg=BLUE, 
            width=20, 
            command=lambda: self.destroy()
        )
        buttonKembali.grid(row=1, column=0, pady=(0, 10))