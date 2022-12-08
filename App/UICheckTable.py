from tkinter import Toplevel, Button, Label, Frame
from .State import get_center
from .Colors import BLUE, RED, GRAY
from .UITableDetail import UITableDetail

WIDTH = 300
HEIGHT = 350

class UICheckTable(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        # Data
        self.table = self.master.db_table
        
        # konfigurasi window
        self.configWindow(WIDTH, HEIGHT)

        # buat komponen ui
        self.initUI()
        
    
    # Cek detail meja
    def getDetail(self, id) -> None:
        if not self.table[id].reserved:
            return
        UITableDetail(self, id)

    # Pemilihan warna tombol tabel
    def getColor(self, id) -> str:
        if not self.table[id].reserved:
            return GRAY
        return RED

    # Ganti warna tombol meja
    def updateTableColorById(self, id) -> None:
        self.buttons[id].config(bg=self.getColor(id))

    # Konfigurasi window
    def configWindow(self, w: int, h: int) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.geometry(get_center(self, w, h))
        self.resizable(False, False)

    # Pembuatan komponen UI
    def initUI(self) -> None:
        # komponen judul
        titleFrame = Frame(self)
        titleLabel = Label(titleFrame, text="Silahkan klik meja kosong yang diinginkan:")
        titleLabel.pack(anchor="center")
        titleFrame.pack(pady=10)

        # komponen meja
        tableFrame = Frame(self)
        row = 0
        self.buttons = []
        for i in range(5):
            row = row + 1
            self.buttons.append(
                Button(
                    tableFrame, 
                    text=i, 
                    width=10, 
                    bg=self.getColor(i),
                    command=lambda i=i: self.getDetail(i))
                )
            self.buttons[i].grid(row=row, column=2, padx=5, pady=5)
        row = 0
        for i in range(5, 10):
            row = row + 1
            self.buttons.append(
                Button(
                    tableFrame, 
                    text=i, 
                    width=10, 
                    bg=self.getColor(i),
                    command=lambda i=i: self.getDetail(i))
                )
            self.buttons[i].grid(row=row, column=4, padx=5, pady=5)
        tableFrame.pack()

        # komponen info meja
        infoFrame = Frame(self)
        infoLabel = Label(infoFrame, text="Info\nMerah: Terisi\nAbu-abu: Kosong\nBiru: Meja anda", justify='left')
        infoLabel.pack(anchor='w', padx=(10, 0))
        infoFrame.pack(fill='x', pady=10)
        

        # komponen navigasi
        buttonFrame = Frame(self)
        buttonKembali = Button(
            buttonFrame, 
            text="Kembali", 
            bg=BLUE, fg="white", 
            width=20, 
            command=self.destroy
        )
        buttonKembali.pack(anchor="center")
        buttonFrame.pack()
        

        

        
        