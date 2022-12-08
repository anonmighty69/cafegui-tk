
class Table:
    def __init__(self, id, customer = None, reserved = False, orderList= None):
        self.id = id
        self.customer = customer
        self.orderList = orderList
        self.reserved = reserved

    # debug
    def value(self):
        order = []
        for i in self.orderList:
            order.append(i.value())
        result = { 'tableid': self.id, 'customerid': self.customer.id, 'order': order, 'reserved': True }
        return result


    

            





    

