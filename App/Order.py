


class Order:
    def __init__(self, menu=None, customer=None, qty=0):
        self.menu = menu
        self.qty = qty
        self.customer = customer

    def value(self):
        result = { 'menuid': self.menu.id, 'qty': self.qty, 'price': self.price }
        return result