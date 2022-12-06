

class Customer:
    def __init__(self, name="dummy", table=None):
        self.table = table
        self.name = name
        self.order = None
        self.payment = 0
