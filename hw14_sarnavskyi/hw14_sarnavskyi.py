import enum


class Constants(enum.Enum):
    TANK_LEVEL = 0
    ODOMETER_VALUE = 0


class Vehicle:
    def __init__(self, producer, model, year, tank_capacity, maxspeed, fuel_consumption):
        self.producer = str(producer)
        self.model = str(model)
        self.year = int(year)
        self.tank_capacity = float(tank_capacity)
        self.tank_level = float(Constants.TANK_LEVEL.value)
        self.maxspeed = int(maxspeed)
        self.fuel_consumption = float(fuel_consumption)
        self.odometer_value = int(Constants.ODOMETER_VALUE.value)

    def __str__(self):
        return f'This car is {self.model}, made in {self.year} and ran {self.odometer_value} kilometers'

    __repr__ = __str__

    def refueling(self):
        if self.tank_capacity > self.tank_level:
            print(f'{self.producer} {self.model}`s tank was filled by {self.tank_capacity - self.tank_level} liters')
            self.tank_level = self.tank_capacity
        else:
            print(f'{self.producer} {self.model}`s tank is already full!')

    def race(self, trip_range):

        trip_data = {}
        if self.tank_level/(self.fuel_consumption/100) >= trip_range:
            trip_data.update({'Trip range': round(trip_range, 2)})
        else:
            trip_data.update({'Trip range': round(self.tank_level/(self.fuel_consumption/100), 2)})

        if self.tank_level - (self.fuel_consumption / 100) * trip_range > 0:
            trip_data.update({'Fuel level left': round(self.tank_level - (self.fuel_consumption/100) * trip_range, 2)})
        else:
            trip_data.update({'Fuel level left': 0})

        # тут я від себе додав обмеження по швидкісному режиму
        if self.maxspeed * 0.8 > 130:
            trip_data.update({'Travel time': round(trip_data.get('Trip range') / 130, 2)})
        else:
            trip_data.update({'Travel time': round(trip_data.get('Trip range') / self.maxspeed * 0.8, 2)})

        self.tank_level = trip_data.get('Fuel level left')
        self.odometer_value += int(trip_data.get('Trip range'))

        return trip_data

    def lend_fuel(self, other):
        if other.tank_level == 0 or self.tank_level == self.tank_capacity:
            print("Dont worry, I will deal with it")
        elif other.tank_level >= self.tank_capacity - self.tank_level:
            difference_level = round(self.tank_capacity - self.tank_level, 2)
            print(f"Thx bro, you saved me. You have dealt me {difference_level} liters of fuel")
            self.tank_level = self.tank_capacity
            other.tank_level -= difference_level
        else:
            print(f"Thx bro, you saved me. You have dealt me {other.tank_level} liters of fuel")
            self.tank_level += other.tank_level
            other.tank_level = 0

    def __eq__(self, other):
        return self.year == other.year and self.odometer_value == other.odometer_value


brothers_car = Vehicle('Ford', 'Mustang', 2019, 61, 250, 9)
leonards_car = Vehicle('Volkswagen', 'Golf', 2021, 50, 228, 6.5)
ambulance_car = Vehicle('Mercedes-Benz', 'Sprinter 319', 2017, 90, 150, 11)


if __name__ == '__main__':
    brothers_car.refueling()
    leonards_car.lend_fuel(brothers_car)
    print(brothers_car.tank_level)
    print(leonards_car.tank_level)

    brothers_car.refueling()
    leonards_car.refueling()
    ambulance_car.refueling()

    brothers_car.race(32)
    brothers_car.race(13)
    brothers_car.race(29)
    print(brothers_car.tank_level)

    leonards_car.race(99)
    print(leonards_car.tank_level)

    ambulance_car.race(5)
    ambulance_car.race(2)
    ambulance_car.race(1)
    ambulance_car.race(12)
    print(ambulance_car.tank_level)

    ambulance_car.lend_fuel(leonards_car)
    leonards_car.refueling()
    print(leonards_car.tank_level)
    print(ambulance_car.tank_level)

    ambulance_car.lend_fuel(brothers_car)
    print(brothers_car.tank_level)
    print(ambulance_car.tank_level)

    print(brothers_car.odometer_value)
    print(leonards_car.odometer_value)
    print(ambulance_car.odometer_value)

    print(brothers_car == leonards_car)
    print(leonards_car == ambulance_car)
