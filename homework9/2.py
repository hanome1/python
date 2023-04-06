class Meta(type):
    def __init__(cls, name, bases, namespace):
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class MyClass(metaclass = Meta):
    pass
obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()
print(obj1 is obj2)
print(obj2 is obj3)
print(obj3 is obj4)
print(obj4 is obj1)