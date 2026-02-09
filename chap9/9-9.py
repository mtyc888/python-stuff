class Car:
    def __init__(self, make, model, year):
                            """Initialize attributes to describe a car."""
                            self.make = make
                            self.model = model
                            self.year = year
                            self.odometer_reading = 0
    def get_descriptive_name(self):
            """Return a neatly formatted descriptive name."""
            long_name = f"{self.year} {self.make} {self.model}"
            return long_name.title()
    def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
            """Set the odometer reading to the given value."""
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
            """Add the given amount to the odometer reading."""
            self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=40):
            """Initialize the battery's attributes."""
            self.battery_size = battery_size
        
        
    def describe_battery(self):
            """Print a statement describing the battery size."""
            print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
            """Print a statement about the range this battery provides. Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery. """
            if self.battery_size == 40:
                range = 150
            elif self.battery_size == 65:
                range = 225
                print(f"This car can go about {range} miles on a full charge.")
            # else:
            #     upgrade_battery(self)
    def upgrade_battery(self):
        if self.battery_size > 65:
                range = 300
                print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
     def __init__(self, make, model, year):
            """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
            super().__init__(make, model, year)
            self.battery = Battery()



my_leaf = ElectricCar('nissan', 'leaf', 2024)

my_leaf.battery = Battery(battery_size=75)

my_leaf.battery.upgrade_battery()

print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()