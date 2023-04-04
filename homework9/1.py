class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name
class Order:
    price = NonNegative()
    quantity = NonNegative()
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity
    def total(self):
        return self.price * self.quantity
apple_order = Order('apple', 1, 10)
apple_order.total()
#apple_order.price = -10
#apple_order.quantity = -10



class ChangeAtr:
    def __init__(self, any_atr):
        self.here_attr = any_atr 
    def __get__(self, example, owner):
        return example.__dict__[self.here_attr] 
    def __set__(self, example, value):
        if value <= 0:
            raise ValueError('Должен быть положительным')
        example.__dict__[self.here_attr] = value 

class Whisky:
    cost = ChangeAtr('cost') 
    size = ChangeAtr('size')
    def __init__(self, name, type, cost, size): 
        self.name = name
        self.type = type
        self.cost = cost
        self.size = size

    def total_cost(self):
        return self.cost * self.size

alco = Whisky('Bells', 'Spiced', 1200, 0.7)
print(alco.total_cost())

alco.cost = 900
alco.size = 5
print(alco.total_cost())