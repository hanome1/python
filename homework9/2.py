class Meta(type):
    a = None
    def __init__(self, clsname, bases, clsdict):
        if a is None:
            a = self
        return a

class MyClass(metaclass = Meta):
    def __init__(self):
        return self
obj1 = MyClass()
obj2 = MyClass()
print(obj1 is obj2)