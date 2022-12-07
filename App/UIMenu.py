from tkinter import Toplevel, Label, Button, Entry, END, ttk
from .State import get_center
from .UITable import UITable
from .Colors import BLUE
from .Order import Order

class UIMenu(Toplevel):
    def __init__(self, master, customer):
        super().__init__(master)
        self.customer = customer
        self.headers = ["Kode", "Nama", "Harga", "Kegurihan", "Jumlah"]
        self.total_price = 0
        self.combobox = []
        self.orderList = []
        self.oncreate()
        
    def update_label(self, id):
        self.label['text'] = f"No meja: {id}"
        
    def update_table(self):
        UITable(self, self.customer, self.master.db_table)

    def oncreate(self):
        self.grab_set()
        self.geometry(get_center(self, 800, 400))
        for column in range(5):
            self.grid_columnconfigure(column, weight=1)
        
        self.set_gui()

    def onselected_combobox(self, event):
        
        sum_price = 0
        orderList = []
        for i, menu in enumerate(self.master.db_menu):
            qty = int(self.combobox[i].get())
            price = menu.price * qty
            sum_price = sum_price + price
            if price:
                order = Order(menu, self.customer, qty, sum_price)
                orderList.append(order)
        
        self.orderList = orderList
        # update total harga
        self.total_price = sum_price
        self.price_label['text'] = f"Total harga: {self.total_price}"


    def set_gui(self):
        Label(self, text=f"Nama pemesan: {self.customer.name}").grid(row=0, column=0, pady=(20, 20))
        self.label = Label(self, text=f"No meja: {self.customer.table.id}")
        self.label.grid(row=0, column=3, sticky="w", pady=(20, 20))
        Button(self, text="Ubah", bg=BLUE, fg="white", command=self.update_table).grid(row=0, column=3, pady=(20, 20))
        
        self.generate_table("MEALS", 1)
        self.generate_table("DRINKS", 5)
        self.generate_table("SIDES", 12)

        self.price_label = Label(self, text=f"Total harga: {self.total_price}")
        self.price_label.grid(row=20, column=4, sticky="w")
        Button(self, text="Kembali", width=30, bg=BLUE, fg="white").grid(row=21, column=1)
        Button(self, text="OK", width=30, bg=BLUE, fg="white", command=self.save_order).grid(row=21, column=3)
        
    def save_order(self):
        id = self.customer.table.id
        
        # update table
        self.master.db_table[id].reserved = True
        self.master.db_table[id].customer = self.customer

        # update customer
        self.customer.table = self.master.db_table[id]
        #self.customer.menu = self.
        self.destroy()
    
    def generate_table(self, category, row_begin):
        Label(self, text=category).grid(row=row_begin, column=0)

        # table headers
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
        
        
        for i, item in enumerate(self.master.db_menu):
            if item.category is not category:
                continue
            for j, var in enumerate(item.values()):
                entry = Entry(self, width=20, fg=BLUE)
                entry.insert(END, var)
                if j == 0:
                    entry.grid(row=row_begin+i+2, column=j, sticky="we", padx=(10, 0))
                else:
                    entry.grid(row=row_begin+i+2, column=j, sticky="we")
            values = tuple([k for k in range(10)])
            quantity = ttk.Combobox(self, values=values)
            quantity.current(0)
            quantity.grid(row=row_begin+i+2, column=len(item.values()), sticky="we", padx=(0, 10))
            quantity.bind("<<ComboboxSelected>>", self.onselected_combobox)
            self.combobox.append(quantity)

        
