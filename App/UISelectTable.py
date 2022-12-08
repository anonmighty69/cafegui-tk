from tkinter import Toplevel, Label, Button, Frame
from .State import get_center
from .Colors import BLUE, RED, GRAY, GREEN

WIDTH = 300
HEIGHT = 350

# Tampilan ganti meja
class UISelectTable(Toplevel):
    def __init__ (self, master, customer, table):
        super().__init__(master)

        # Data
        self.customer = customer
        self.table = table
        self.selected = -1

        # konfigurasi window
        self.configWindow(WIDTH, HEIGHT)

        # tampil ui
        self.initUI()

    # Pilih warna
    def getColor(self, id) -> str:
        if self.customer.table.id == id:
            return BLUE
        elif self.table[id].reserved is True:
            return RED
        else:
            return GRAY

    # Konfigurasi window
    def configWindow(self, w: int, h: int) -> None:
        self.title("Kafe Daun-Daun")
        self.grab_set()
        self.geometry(get_center(self, w, h))
        self.resizable(False, False)

    # Tampil UI
    def initUI(self) -> None:
        # komponen judul
        frameTitle = Frame(self)
        titleLabel = Label(frameTitle, text="Silahkan klik meja kosong yang diinginkan:")
        titleLabel.pack(anchor="center")
        frameTitle.pack(pady=10)
        row = 0
        # komponen meja
        frameTable = Frame(self)
        row = 0
        self.buttons = []
        for i in range(5):
            row = row + 1
            self.buttons.append(
                Button(
                    frameTable, 
                    text=i, 
                    width=10, 
                    bg=self.getColor(i),
                    command=lambda i=i: self.selectTable(i))
                )
            self.buttons[i].grid(row=row, column=2, padx=5, pady=5)
        row = 0
        for i in range(5, 10):
            row = row + 1
            self.buttons.append(
                Button(
                    frameTable, 
                    text=i, 
                    width=10, 
                    bg=self.getColor(i),
                    command=lambda i=i: self.selectTable(i))
                )
            self.buttons[i].grid(row=row, column=4, padx=5, pady=5)
        frameTable.pack()

        # komponen info meja
        frameInfo = Frame(self)
        infoLabel = Label(frameInfo, text="Info\nMerah: Terisi\nAbu-abu: Kosong\nBiru: Meja anda", justify='left')
        infoLabel.pack(anchor='w', padx=(10, 0))
        frameInfo.pack(fill='x', pady=10)

        # komponen navigasi
        frameButton = Frame(self)
        buttonKembali = Button(
            frameButton, 
            text="Kembali", 
            bg=BLUE, fg="white", 
            width=15, 
            command=self.onCloseWindow
        )
        buttonKembali.grid(row=0, column=1, padx=10)
        buttonOk = Button(
            frameButton, 
            text="OK", 
            bg=BLUE, 
            fg="white", 
            width=15, 
            command=lambda: self.onChangeTable(self.selected)
        )
        buttonOk.grid(row=0, column=2, padx=10)
        frameButton.pack()

        

    # Ganti meja pembeli
    def onChangeTable(self, id) -> None:
        if self.customer.table.id == id or self.table[id].reserved or self.selected == -1:
            pass
        else:
            self.customer.table.reserved = False
            self.table[id].reserved = True
            self.customer.table = self.table[id]
            self.master.updateLabel(id)
            self.onCloseWindow()

    def onCloseWindow(self):
        self.master.grab_set()
        self.destroy()


    # Pilih meja pembeli
    def selectTable(self, id) -> None:
        if self.customer.table.id == id or self.table[id].reserved:
            return
        if self.selected == -1:
            self.selected = id
            self.buttons[self.selected].config(bg=GREEN)
        else:
            self.buttons[self.selected].config(bg=GRAY)
            self.selected = id
            self.buttons[id].config(bg=GREEN)
        


        

        