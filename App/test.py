from tkinter import Tk
import re
from .table import Table
JUMLAH_TABEL = 10

class Window(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.db_menu = open('menu.txt', 'r')

        self.db_table = []
        for i in range(JUMLAH_TABEL):
            self.db_table.append(Table(i))

        self.oncreate()

    def oncreate(self) -> None:
        self.title("Cafe Daun-Daun")
        


    def update(self) -> None:
        self.mainloop()

    def load_data(self, pathname):
        file = open(pathname, 'r')
        title_pattern = "===([A-Z]+)"
        title = []
        menu = []

        # search title and data row
        for line in file.read().splitlines():
            match = re.search(title_pattern, line)
            if match:
                matched_title = match.group(1)[:]
                title.append(matched_title)
            else:
                menu.append(line.split(";"))

        return title, menu





