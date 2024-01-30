

class Car:
    """A simple attempt to represent a car."""

    def __init__(self , make, model, year):
        """Initialize attributes to describe a car"""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a neatly formated printed name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """prints the statement for showing the cars milage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value reject the 
        change if it attempts to roll the odometer back
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        
        else:
            print("You cant roll back on an odometer!!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

class Battery:
    """A simple attempt to create the battery class"""

    def __init__(self,battery_size = 40):
        """Intitializes the batteries size"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Initializes the description of the battery size"""
        print(f"This size of the battery is {self.battery_size}-kwh battery")

    def get_range(self):
        """Print a statement about the range"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"this car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Represents aspects of an Electric Car"""
    
    def __init__(self, make, model, year):
        """Initializes attributes of the parent class
        The initialized attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery life"""
        print(f"this car has a {self.battery}-kwh battery")

    def fill_gas(self):
        """Electric vehicles dont have gas tanks"""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar('nissian','leaf','2024')
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()


my_new_car = Car('audi','a4','2024')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_used_car = Car('subaru','outback',2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()