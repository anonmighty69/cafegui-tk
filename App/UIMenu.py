from tkinter import Toplevel, Label, Button, Entry, END
from .State import get_center
from .UITable import UITable
from .Colors import BLUE

class UIMenu(Toplevel):
    def __init__(self, master, customer):
        super().__init__(master)
        self.customer = customer
        self.headers = ["Kode", "Nama", "Harga", "Kegurihan", "Jumlah"]
        self.oncreate()
        
    def update_label(self, idx):
        self.label['text'] = idx
        
    def update_table(self):
        UITable(self, self.customer, self.master.db_table)

    def oncreate(self):
        self.grab_set()
        self.geometry(get_center(self, 1280, 720))
        for column in range(5):
            self.grid_columnconfigure(column, weight=1)

        self.set_gui()

    def set_gui(self):
        Label(self, text=f"Nama pemesan: {self.customer.name}").grid(row=0, column=0, pady=(100, 50))
        self.label = Label(self, text=f"No meja: {self.customer.table.idx}")
        self.label.grid(row=0, column=3, sticky="w", pady=(100, 50))
        Button(self, text="Ubah", bg="#4472C4", fg="white", command=lambda: self.update_table()).grid(row=0, column=3, pady=(100, 50))
        
        self.generate_headers("MEALS", 1)
        self.generate_item()
        self.generate_headers("DRINKS", 5)
        self.generate_headers("SIDES", 9)

    def generate_item(self):
        pass

    def generate_headers(self, title, row_begin):
        Label(self, text=title).grid(row=row_begin, column=0)
        for idx, item in enumerate(self.headers):
            entry = Entry(self, width=20, fg=BLUE)
            entry.insert(END, item)
            entry['state'] = 'readonly'
            if idx == 0:
                entry.grid(row=row_begin+1, column=idx, sticky="we", padx=(10, 0))
            elif idx == len(self.headers)-1:
                entry.grid(row=row_begin+1, column=idx, sticky="we", padx=(0, 10))
            else:
                entry.grid(row=row_begin+1, column=idx, sticky="we")