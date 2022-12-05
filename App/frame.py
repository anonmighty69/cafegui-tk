from tkinter import Button, ttk, Toplevel, Label, Entry
from .utils import get_center

class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Background frame
        s = ttk.Style()
        s.configure('Main.TFrame', background="#417D7A")
        self.configure(style='Main.TFrame')
        self.grid(row=0, column=0, sticky="nsew")

        # Button
        Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white").grid(row=0, column=0, pady=(120, 50))
        Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white").grid(row=1, column=0)

        # Grid config
        self.grid_columnconfigure(0, weight=1)

    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        pass

class BuatPesanan(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.grab_set()
        self.title("Kafe Daun-Daun")
        self.geometry(get_center(self, 400, 200))
        Label(self, text="Siapa nama Anda?").grid(row=0, column=0)
        Entry(self).grid(row=0, column=1)
        Button(self, text="Kembali", bg="#4472C4", fg="white", command=lambda: self.destroy()).grid(row=1, column=0, sticky="we", padx=(20, 10), pady=(0, 10))
        Button(self, text="Lanjut", bg="#4472C4", fg="white").grid(row=1, column=1, sticky="we", padx=(10, 20), pady=(0, 10))


        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
    
    def tampil_menu(self):
        pass

class Menu(ttk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        

        