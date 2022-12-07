from tkinter import Toplevel, Label, Button, Entry
from .State import get_center
from .UIMenu import UIMenu
from .Customer import Customer

class UIOrder(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.oncreate()
    
    def show_menu(self, name):
        self.destroy()
        customer = Customer(name, self.getRandomTable())
        UIMenu(self.master, customer)

    def getRandomTable(self):
        table = None
        for id, table in enumerate(self.master.db_table):
            if not table.reserved:
                table = self.master.db_table[id]
                break
        return table
                

    def oncreate(self):
        self.grab_set()
        self.title("Kafe Daun-Daun")
        self.geometry(get_center(self, 400, 200))
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.set_gui()

    def set_gui(self):
        Label(self, text="Siapa nama Anda?").grid(row=0, column=0)
        name = Entry(self)
        name.grid(row=0, column=1)
        Button(self, text="Kembali", bg="#4472C4", fg="white", command=lambda: self.destroy()).grid(row=1, column=0, sticky="we", padx=(20, 10), pady=(0, 10))
        Button(self, text="Lanjut", bg="#4472C4", fg="white", command=lambda: self.show_menu(name.get())).grid(row=1, column=1, sticky="we", padx=(10, 20), pady=(0, 10))
