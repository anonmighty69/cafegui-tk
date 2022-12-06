from tkinter import Toplevel, Label, Button
from .State import get_center
from .Colors import BLUE, RED, GRAY, GREEN

class UITable(Toplevel):
    def __init__ (self, master, customer, table):
        super().__init__(master)
        self.customer = customer
        self.table = table
        self.selected = -1
        self.oncreate()

    def getcolor(self, idx):
        color = ""
        if self.customer.table.idx == idx:
            color = BLUE
        elif self.table[idx].reserved is True:
            color = RED
        else:
            color = GRAY
        return color

    def oncreate(self):
        self.grab_set()
        self.geometry(get_center(self, 600, 250))
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        
        self.set_gui()

    def set_gui(self):
        Label(self, text="Silahkan klik meja kosong yang diinginkan:").grid(row=0, column=3)
        row = 0
        self.buttons = []
        for i in range(5):
            row = row + 1
            self.buttons.append(Button(self, text=i, width=10, bg=self.getcolor(i), command=lambda i=i: self.select_table(i)))
            self.buttons[i].grid(row=row, column=2)
        row = 0
        for i in range(5, 10):
            row = row + 1
            self.buttons.append(Button(self, text=i, width=10, bg=self.getcolor(i), command=lambda i=i: self.select_table(i)))
            self.buttons[i].grid(row=row, column=4)
        
        Label(self, text="Info\nMerah: Terisi\nAbu-abu: Kosong\nBiru: Meja anda",anchor="w").grid(row=6, column=0, columnspan=5)
        Button(self, text="Kembali", bg=BLUE, fg="white", width=20).grid(row=7, column=2, padx=(10,0))
        Button(self, text="OK", bg=BLUE, fg="white", width=20, command=lambda:self.change_table(self.selected)).grid(row=7, column=4, padx=(0,10))

    def change_table(self, idx):
        if self.customer.table.idx == idx or self.table[idx].reserved or self.selected == -1:
            pass
        else:
            self.customer.table.reserved = False
            self.table[idx].reserved = True
            self.customer.table = self.table[idx]
            self.master.update_label(idx)
        self.master.grab_set()
        self.destroy()

    def select_table(self, idx):
        if self.customer.table.idx == idx or self.table[idx].reserved:
            return
        if self.selected == -1:
            self.selected = idx
            self.buttons[self.selected].config(bg=GREEN)
        else:
            self.buttons[self.selected].config(bg=GRAY)
            self.selected = idx
            self.buttons[idx].config(bg=GREEN)
        print(self.selected)
        


        

        