from tkinter import Toplevel, Label, Button, Entry, END, ttk
from .State import get_center
from .UISelectTable import UISelectTable
from .Colors import BLUE
from .Order import Order

WIDTH = 800
HEIGHT = 400
class UISelectMenu(Toplevel):
    def __init__(self, master, customer):
        super().__init__(master)
        
        # Data
        self.customer = customer
        self.total_price = 0
        self.combobox = []
        self.orderList = []

        # konfigurasi window
        self.configWindow(WIDTH, HEIGHT)

        # tampil ui
        self.initUI()
    

    def updateLabel(self, id: int) -> None:
        self.label['text'] = f"No meja: {id}"

    

    # Konfigurasi window
    def configWindow(self, w: int, h: int) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.geometry(get_center(self, w, h))
        self.resizable(False, False)
        for column in range(5):
            self.grid_columnconfigure(column, weight=1)

    # Tampil ui
    def initUI(self) -> None:
        Label(self, text=f"Nama pemesan: {self.customer.name}").grid(row=0, column=0, pady=(20, 20))
        self.label = Label(self, text=f"No meja: {self.customer.table.id}")
        self.label.grid(row=0, column=3, sticky="w", pady=(20, 20))
        Button(self, text="Ubah", bg=BLUE, fg="white", command=self.onUpdateTable).grid(row=0, column=3, pady=(20, 20))
        
        self.generate_table("MEALS", 1)
        self.generate_table("DRINKS", 5)
        self.generate_table("SIDES", 12)

        self.labelHarga = Label(self, text=f"Total harga: {self.total_price}")
        self.labelHarga.grid(row=20, column=4, sticky="w")

        buttonKembali = Button(
            self, 
            text="Kembali", 
            width=30, 
            bg=BLUE, 
            fg="white",
            command=self.onCloseWindow
        )
        buttonKembali.grid(row=21, column=1)
        buttonOk = Button(
            self, 
            text="OK", 
            width=30, 
            bg=BLUE, 
            fg="white", 
            command=self.saveOrder
        )
        buttonOk.grid(row=21, column=3)
        
    # Simpan pesanan
    def saveOrder(self) -> None:
        id = self.customer.table.id
        # isi data meja
        self.master.db_table[id].reserved = True
        self.master.db_table[id].customer = self.customer
        self.master.db_table[id].orderList = self.orderList

        # ubah tabel pembeli
        self.customer.table = self.master.db_table[id]
        self.master.grab_set()
        self.destroy()
    
    # Pilih header
    def getheader(self, category) -> tuple:
        if category == "MEALS":
            return ("Kode", "Nama", "Harga", "Kegurihan", "Jumlah")
        elif category == "DRINKS":
            return ("Kode", "Nama", "Harga", "Kemanisan", "Jumlah")
        else:
            return ("Kode", "Nama", "Harga", "Keviralan", "Jumlah")

    # Tampil tabel
    def generate_table(self, category, row_begin):
        Label(self, text=category).grid(row=row_begin, column=0)
        headers = self.getheader(category)
        # table headers
        for idx, item in enumerate(headers):
            entry = Entry(self, width=20)
            entry.insert(END, item)
            entry['state'] = 'readonly'
            if idx == 0:
                entry.grid(row=row_begin+1, column=idx, sticky="we", padx=(10, 0))
            elif idx == len(headers)-1:
                entry.grid(row=row_begin+1, column=idx, sticky="we", padx=(0, 10))
            else:
                entry.grid(row=row_begin+1, column=idx, sticky="we")
        
        
        for i, item in enumerate(self.master.db_menu):
            if item.category is not category:
                continue
            for j, var in enumerate(item.values()):
                entry = Entry(self, width=20)
                entry.insert(END, var)
                if j == 0:
                    entry.grid(row=row_begin+i+2, column=j, sticky="we", padx=(10, 0))
                else:
                    entry.grid(row=row_begin+i+2, column=j, sticky="we")
                entry['state'] = 'readonly'
            values = tuple([k for k in range(10)])
            quantity = ttk.Combobox(self, values=values)
            quantity.current(0)
            quantity['state'] = 'readonly'
            quantity.grid(row=row_begin+i+2, column=len(item.values()), sticky="we", padx=(0, 10))
            quantity.bind("<<ComboboxSelected>>", self.onSelectComboBox)
            self.combobox.append(quantity)

##################### EVENT REGION #############################
    # Tampil pilihan tabel  
    def onUpdateTable(self) -> None:
        UISelectTable(self, self.customer, self.master.db_table)

    # Ubah total harga
    def onSelectComboBox(self, event):
        sum_price = 0
        orderList = []
        for i, menu in enumerate(self.master.db_menu):
            qty = int(self.combobox[i].get())
            price = menu.price * qty
            sum_price = sum_price + price
            if price:
                order = Order(menu, self.customer, qty)
                orderList.append(order)
        self.orderList = orderList

        # update total harga
        self.total_price = sum_price
        self.labelHarga['text'] = f"Total harga: {self.total_price}"

    def onCloseWindow(self) -> None:
        self.destroy()

        
