#Name: Naylene Rondon
#Date: 3/29/17
#Purpose: Classes - Object Orientation

class Car():
    """An attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initisalize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted decriptive name."""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("The " + self.model + " has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Update odometer. Reject if it's decreasing."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add miles to the odometer."""
        self.odometer_reading += miles
    

my_new_car = Car("audi", "a4", 2016)
my_old_car = Car("Toyota", "Yaris", 2010)
print("I bought a new car.")
print("It is a " + my_new_car.get_descriptive_name() + ".")
my_new_car.read_odometer()

#Modify attribute via Meta
print("My old car was a " + my_old_car.get_descriptive_name() + ".")
my_old_car.odometer_reading = 45678
my_old_car.read_odometer()

#Driving Simulation
print("I drove around town.")
my_new_car.update_odometer(35)
my_new_car.read_odometer()

#Error Test
my_old_car.update_odometer(5)

#Driving Simulation
print("I drove to Miami in my new car.")
my_new_car.increment_odometer(135)
my_new_car.read_odometer()
