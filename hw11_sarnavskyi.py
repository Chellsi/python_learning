# task1
# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель",
# наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".

class Transport:
    def __init__(self, movement_type, purpose_type):
        self.movement_type = movement_type
        self.purpose_type = purpose_type


class Car(Transport):
    def __init__(self, movement_type, purpose_type, manufacturer, model, year_of_issue):
        super().__init__(movement_type, purpose_type)
        self.manufacturer = manufacturer
        self.model = model
        self.year_of_issue = year_of_issue


class Aircraft(Transport):
    def __init__(self, movement_type, purpose_type, model, seats_count):
        super().__init__(movement_type, purpose_type)
        self.model = model
        self.seats_count = seats_count


class Ship(Transport):
    def __init__(self, movement_type, purpose_type, cargo_passanger_type, registration_name, registration_flag):
        super().__init__(movement_type, purpose_type)
        self.cargo_passanger_type = cargo_passanger_type
        self.registration_name = registration_name
        self.registration_flag = registration_flag



fathers_car = Car('drive', 'civilian', 'Sitroen', 'Berlingo', 2008)
flight_to_Vienna = Aircraft('flight', 'civilian', 'Embraer 195', 120)
corn_cargo_wessel = Ship('sail', 'civilian', 'cargo', 'E-SHIP 1', 'Germany')
