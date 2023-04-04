from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for key, value in self.__color.items():
            print(key)
            sleep(value)

traf = TrafficLight(color={
    "Красный": 7,
    "Желтый": 2,
    "Зеленый": 7})
traf.running()