from tkinter import Tk
from .UIMain import UIMain
from .Menu import Drinks, Meals, Sides
from .Table import Table
import re

JUMLAH_TABEL = 10
PATH = "menu.txt"

class App(Tk):
    def __init__(self):
        super().__init__()
        self.db_table = ([Table(i) for i in range(JUMLAH_TABEL)])

        self.db_menu = []
        file = open(PATH, 'r')
        title_pattern = "===([A-Z]+)"
        matched_title = ""
        for line in file.read().splitlines():
            match = re.search(title_pattern, line)
            menu = None
            if match:
                matched_title = match.group(1)[:]
            else:
                menu = line.split(";")
                new_menu = None
                if matched_title == "MEALS":
                    new_menu = Meals(menu[0], menu[1], menu[2], menu[3])
                elif matched_title == "DRINKS":
                    new_menu = Drinks(menu[0], menu[1], menu[2], menu[3])
                else:
                    new_menu = Sides(menu[0], menu[1], menu[2], menu[3])
                self.db_menu.append(new_menu)
        UIMain(self)

    def run(self):
        self.mainloop()


