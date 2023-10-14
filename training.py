class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f'{self.make} {self.model} {self.year}'
        return full_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('You cant roll back an odometer!!!')

    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print('You cant roll back an odometer!!!')


class Battery:

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size} kWh battery')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")


class ElectroCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


elc_car = ElectroCar('Tesla', 'Model 3', 2022)
print(elc_car.get_descriptive_name())
elc_car.battery.describe_battery()
elc_car.battery.get_range()


# car1 = Car('Audi', 'A7', 2020)
# print(car1.get_descriptive_name())
# car1.read_odometer()
#
# car1.update_odometer(1000)
# car1.read_odometer()
#
# car1.increment_odometer(123)
# car1.read_odometer()
#
# car1.update_odometer(10)
# car1.read_odometer()
#
# car1.increment_odometer(-3)
# car1.read_odometer()
