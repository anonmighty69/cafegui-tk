


class Menu:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = int(price)

class Meals(Menu):
    def __init__(self, id, name, price, tingkat_kegurihan):
        super().__init__(id, name, price)
        # TODO handle info tambahan
        self.category = "MEALS"
        self.level = tingkat_kegurihan
    def values(self):
        return self.id, self.name, self.price, self.level

class Drinks(Menu):
    def __init__(self, id, name, price, tingkat_kemanisan):
        super().__init__(id, name, price)
        # TODO handle info tambahan
        self.category = "DRINKS"
        self.level = tingkat_kemanisan
    def values(self):
        return self.id, self.name, self.price, self.level

class Sides(Menu):
    def __init__(self, id, name, price, tingkat_keviralan):
        super().__init__(id, name, price)
        # TODO handle info tambahan
        self.category = "SIDES"
        self.level = tingkat_keviralan
    def values(self):
        return self.id, self.name, self.price, self.level