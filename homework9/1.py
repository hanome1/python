class NonNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
class Order:
    price = NonNegative()
    quantity = NonNegative()
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
apple_order = Order('apple', 1, 10)
#apple_order.price = -10
#apple_order.quantity = -10



class GottaBeNum:
    def __set__(self, instance, value):
        if isinstance(value, str):
            raise ValueError('Должен быть числом')

class Whisky:
    cost = GottaBeNum() 
    size = GottaBeNum()
    def __init__(self, name, type, cost, size): 
        self.name = name
        self.type = type
        self.cost = cost
        self.size = size
alco = Whisky('Bells', 'Spiced', 1200, 0.7)

#alco.cost = 'sss'
#alco.size = 'sss'