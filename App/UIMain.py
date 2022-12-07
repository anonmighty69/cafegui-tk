from tkinter import Button, ttk
from .UIOrder import UIOrder
from .State import get_center
from .UIFull import UIFull

class UIMain(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.oncreate()

    def buat_pesanan(self):
        isReserved = False
        for table in self.master.db_table:
            if not table.reserved:
                isReserved = True
                break
        if isReserved:
            UIOrder(self.master)
        else:
            UIFull(self.master)
        
    def check_table(self):
        for table in self.master.db_table:
            if not table.reserved:
                return True
        return False

        
    def selesai_gunakan_meja(self):
        pass
    
    def oncreate(self):
        self.master.geometry(get_center(self, 600, 400))
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.set_gui()

    def set_gui(self):
        Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white").grid(row=0, column=0, pady=(120, 50))
        Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white").grid(row=1, column=0)

    





        
        
        

        