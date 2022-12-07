
class Customer:
    count = 0
    def __init__(self, name = "", table = None, order = None):
        self.id = Customer.count
        self.name = name
        self.table = table
        self.order = order
        Customer.count += 1
