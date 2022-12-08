from tkinter import Toplevel, Label, Button, Entry
from .State import get_center
from .UISelectMenu import UISelectMenu
from .Customer import Customer
from .Colors import BLUE, WHITE
class UIOrder(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        # konfigurasi window
        self.configWindow()

        # tampil ui
        self.initUI()
    

    # Pilih meja untuk pembeli
    def getRandomTable(self) -> None:
        table = None
        for id, table in enumerate(self.master.db_table):
            if not table.reserved:
                table = self.master.db_table[id]
                break
        return table
                
    # Konfigurasi window
    def configWindow(self) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.geometry(get_center(self, 400, 200))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    # Tampil UI
    def initUI(self) -> None:
        labelPertanyaan = Label(self, text="Siapa nama Anda?")
        labelPertanyaan.grid(row=0, column=0)
        entryNama = Entry(self)
        entryNama.grid(row=0, column=1)

        buttonKembali = Button(
            self, 
            text="Kembali", 
            bg=BLUE, 
            fg=WHITE, 
            command=self.destroy
        )
        buttonKembali.grid(row=1, column=0, sticky="we", padx=(20, 10), pady=(0, 10))

        buttonLanjut = Button(
            self, 
            text="Lanjut", 
            bg=BLUE, 
            fg=WHITE, 
            command=lambda: self.onShowMenu(entryNama.get())
        )
        buttonLanjut.grid(row=1, column=1, sticky="we", padx=(10, 20), pady=(0, 10))
        self.bind('<Return>', lambda e: self.onEnterPressed(e, entryNama.get()))
        self.bind('<Escape>', self.onEscapePressed)
############### EVENT REGION ###############

    # Tampil pemilihan menu
    def onShowMenu(self, name: str) -> None:
        customer = Customer(name, self.getRandomTable())
        UISelectMenu(self.master, customer)
        self.destroy()

    def onEnterPressed(self, e, name):
        self.onShowMenu(name)
    
    def onEscapePressed(self, e):
        self.destroy()
    
    