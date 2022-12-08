from tkinter import Button, Frame
from .UIOrder import UIOrder
from .State import get_center
from .UIFull import UIFull
from .UICheckTable import UICheckTable
from .Colors import BLUE, WHITE

WIDTH = 600
HEIGHT = 400

# Tampilan awal
class UIMain(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # konfigurasi window
        self.configWindow()

        # komponen ui
        self.initUI()

    # Buat Pesanan
    def onCreateOrder(self) -> None:
        # Check seluruh meja
        isReserved = False
        for table in self.master.db_table:
            if not table.reserved:
                isReserved = True
                break

        # Check ketersediaan meja
        if isReserved:
            UIOrder(self.master)
        else:
            UIFull(self.master)

    # Selesai Gunakan Meja
    def onCheckTable(self) -> None:
        UICheckTable(self.master)

    # Konfigurasi window
    def configWindow(self) -> None:
        self.master.title("Kafe Daun-Daun")
        self.master.resizable(width=False, height=False)
        self.master.geometry(get_center(self, WIDTH, HEIGHT))

    # Tampil UI
    def initUI(self) -> None:
        buttonBuat = Button(
            self, 
            text="Buat Pesanan", 
            width=30, 
            command=self.onCreateOrder, 
            bg=BLUE, 
            fg=WHITE
        )
        buttonBuat.place(relx=.5, rely=.40, anchor='center')
        buttonSelesai = Button(
            self, 
            text="Selesai Gunakan Meja", 
            width=30, 
            command=self.onCheckTable, 
            bg=BLUE, 
            fg=WHITE
        )
        buttonSelesai.place(relx=.5, rely=.50, anchor='center')
        self.pack(fill='both', expand=True)

    





        
        
        

        