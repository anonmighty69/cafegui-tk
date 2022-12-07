


class Order:
    def __init__(self, menu=None, customer=None, qty=0, totalPrice=0):
        self.menu = menu
        self.customer = customer
        self.qty = qty
        self.totalPrice = totalPrice