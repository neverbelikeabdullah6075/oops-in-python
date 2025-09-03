# ✅ CLASS: Blueprint for creating objects
class Car:
    total_car = 0  # ✅ Class variable shared by all instances

    # ✅ Constructor: Initializes object attributes
    def __init__(self, brand, model):
        self.__brand = brand       # ✅ Encapsulation: private attribute
        self.__model = model       # ✅ Encapsulation: private attribute
        Car.total_car += 1         # ✅ Tracks total cars created
        Car.name_len=len(self.full_name())

    # ✅ Static Method: Belongs to class, not instance
    @staticmethod
    def generaldescrip():
        return "Cars are amazing and means of transport"

    # ✅ Property Decorator: Allows method to be accessed like an attribute
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,new_model):
        self.__model=new_model

    # ✅ Getter for private brand
    def get_brand(self):
        return self.__brand

    # ✅ Instance Method: Combines brand and model
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    # ✅ Polymorphism: Can be overridden in child classes
    def fuel_type(self):
        return "petrol or diesel"


# ✅ INHERITANCE: Electric_car inherits from Car
class Electric_car(Car):
    def __init__(self, brand, model, batterysize):
        self.batterysize = batterysize
        super().__init__(brand, model)  # ✅ Calls parent constructor

    def fuel_type(self):  # ✅ Polymorphism: Overrides parent method
        return "electric charge"


# ✅ MULTIPLE INHERITANCE: Battery and Engine classes
class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def Engine_info(self):
        return "This is engine"

# ✅ ElectricCarTwo inherits from Battery, Engine, and Car
class ElectricCarTwo(Battery, Engine, Car):
    pass


# ✅ Creating instances and testing functionality
my_ev = ElectricCarTwo("ev", "2025")
print(my_ev.battery_info())  # Output: This is battery

my_car = Car("toyota", "Corolla")
print(my_car.model)          # Output: Corolla
print(my_car.full_name())    # Output: toyota Corolla

my_newcar = Car("honda", "civic")
print(my_newcar.model)       # Output: civic

# ✅ Inheritance and isinstance checks
my_tesla = Electric_car("tesla", "2025", "85kwh")
print(isinstance(my_tesla, Car))          # Output: True
print(isinstance(my_tesla, Electric_car)) # Output: True
print(my_tesla.model)                     # Output: 2025
print(my_tesla.batterysize)              # Output: 85kwh
print(my_tesla.full_name())              # Output: tesla 2025

# ✅ Encapsulation: Accessing private brand via getter
print(my_car.get_brand())                # Output: toyota

# ✅ Polymorphism: Same method, different behavior
fuel = Car("tesla", "2025")
print(fuel.fuel_type())                  # Output: petrol or diesel

fuel = Electric_car("tesla", "2025", "85kwh")
print(fuel.fuel_type())                  # Output: electric charge

# ✅ Class variable: Shared across all instances
print(Car.total_car)                     # Output: Total cars created
print(my_tesla.total_car)                # Same as above

# ✅ Static method: Accessible via instance or class
print(my_newcar.generaldescrip())        # Output: Cars are amazing...
print(Car.generaldescrip())              # Same output

# ✅ Property decorator: Accessing model like an attribute
my_car.model = "china"
print(my_car.model)# ❌ Error: No setter defined
print(int((Car.name_len())))

# 1. Add a setter to the `model` property so you can change the model name.
# 2. Create a method in Car that returns how many characters are in the full name.
# 3. Add a method in Electric_car that returns battery health as "Good".
# 4. Create a new class `HybridCar` that inherits from both `Engine` and `Electric_car`.
# 5. Add a class method to Car that returns total_car in a formatted string like "Total cars: 5".
# 6. Use isinstance() to check if my_ev is an instance of Battery.
# 7. Add a method in Car that compares two cars and returns True if their models match.