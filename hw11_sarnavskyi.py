# task1
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    made_of = None
    type = None

    def __init__(self, made_of, type):
        self.made_of = made_of
        self.type = type


class Car(Transport):
    wheels_count = 4
    max_speed = 200
    doors_count = 4


class Aircraft(Transport):
    wheels_count = 2
    max_speed = 900
    doors_count = 2


class Ship:
    wheels_count = 0
    max_speed = 60
    doors_count = 2


titanic = Ship
civic = Car
boeing_737 = Aircraft

