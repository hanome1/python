class Road:
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weigth = 25
        self.tickness = 0.05
    def mass(self):
        result = self._length * self._width * self.weigth * self.tickness / 1000
        return print(result)

example_road = Road(5000, 20)
example_road.mass()