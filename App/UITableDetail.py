from tkinter import Toplevel, Label, Button, Entry, END
from .Colors import BLUE
from .State import get_center
from .Table import Table

WIDTH = 800
HEIGHT = 400

class UITableDetail(Toplevel):
    def __init__(self, master, id):
        super().__init__(master)

        # Data
        self.table = self.master.master.db_table[id]
        self.menu = self.master.master.db_menu

        # konfigurasi window
        self.configWindow(WIDTH, HEIGHT)

        # tampil ui
        self.initUI()

    # Konfigurasi window
    def configWindow(self, w: int, h: int) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.geometry(get_center(self, w, h))
        for column in range(5):
            self.grid_columnconfigure(column, weight=1)
        
    # Harga total
    def getTotalPrice(self) -> int:
        sum_price = 0
        for order in self.table.orderList:
            price = order.menu.price * order.qty
            sum_price = sum_price + price
        return sum_price

    # Tampil UI
    def initUI(self) -> None:
        labelNamaPemesan = Label(self, text=f"Nama pemesan: {self.table.customer.name}")
        labelNamaPemesan.grid(row=0, column=0, pady=(20, 20))
        
        labelNomorMeja = Label(self, text=f"No meja: {self.table.id}")
        labelNomorMeja.grid(row=0, column=3, sticky="w", pady=(20, 20))
        
        self.generateTable("MEALS", 1)
        self.generateTable("DRINKS", 5)
        self.generateTable("SIDES", 12)
        
        labelHarga = Label(self, text=f"Total harga: {self.getTotalPrice()}")
        labelHarga.grid(row=20, column=4, sticky="w")
        
        buttonKembali = Button(
            self, 
            text="Kembali", 
            width=30, 
            bg=BLUE, 
            fg="white",
            command=self.onCloseWindow
        )
        buttonKembali.grid(row=21, column=1)

        buttonSelesai = Button(
            self, 
            text="Selesai Gunakan Meja", 
            width=30, bg=BLUE, 
            fg="white", 
            command=self.freeTable
        )
        buttonSelesai.grid(row=21, column=3)

    # Mengosongkan meja
    def freeTable(self) -> None:
        new_table = Table(self.table.id)
        self.master.master.db_table[self.table.id] = new_table
        self.master.updateTableColorById(self.table.id)
        self.master.grab_set()
        self.destroy()

    # Tampil tabel
    def generateTable(self, category, row_begin) -> None:
        labelKategory = Label(self, text=category)
        labelKategory.grid(row=row_begin, column=0)

        # tampil header
        row_begin += 1
        headers = self.getHeader(category)
        for i, item in enumerate(headers):
            entry = Entry(self, width=20)
            entry.insert(END, item)
            entry['state'] = 'readonly'
            if i == 0:
                entry.grid(row=row_begin, column=i, sticky="we", padx=(10, 0))
            elif i == len(headers)-1:
                entry.grid(row=row_begin, column=i, sticky="we", padx=(0, 10))
            else:
                entry.grid(row=row_begin, column=i, sticky="we")

        row_begin += 1
        # tampil menu
        for i, item in enumerate(self.menu):
            if item.category is not category:
                continue
            for j, var in enumerate(item.values()):
                entry = Entry(self, width=20)
                entry.insert(END, var)
                if j == 0:
                    entry.grid(row=row_begin+i, column=j, sticky="we", padx=(10, 0))
                else:
                    entry.grid(row=row_begin+i, column=j, sticky="we")
                entry['state'] = 'readonly'
            
            quantity = Entry(self, width=20)
            value = 0
            for order in self.table.orderList:
                if item.id is order.menu.id:
                    value = order.qty
                    
            quantity.insert(END, value)
            quantity['state'] = 'readonly'
            quantity.grid(row=row_begin+i, column=len(item.values()), sticky="we", padx=(0, 10))

    # Cek header tabel
    def getHeader(self, category) -> tuple:
        if category == "MEALS":
            return ("Kode", "Nama", "Harga", "Kegurihan", "Jumlah")
        elif category == "DRINKS":
            return ("Kode", "Nama", "Harga", "Kemanisan", "Jumlah")
        else:
            return ("Kode", "Nama", "Harga", "Keviralan", "Jumlah")

    # Keluar window / dtor
    def onCloseWindow(self) -> None:
        self.master.grab_set()
        self.destroy()
