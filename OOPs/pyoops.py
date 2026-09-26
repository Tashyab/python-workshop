import copy
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    ride_or_die = True
    def __init__(self) -> None:
        super().__init__()
        self.wheels = None

    @abstractmethod
    def total_wheels(self):
        pass

# Creating Class
class Car(Vehicle):
    # Constructor
    def __init__(self, name, color, price) -> None:
        super().__init__()
        self.name = name
        self.color = color
        self.price = price
        self.wheels = 4

    def total_wheels(self):
        return self.wheels

    # Method Overloading
    def color_love(self, col=None):
        if col:
            print(f"I love the {col} {self.name}.")
        else:
            print(f"I love the {self.color} {self.name}.")

    # Operator Overloading
    def __add__(self, other):
        return self.name + other

    # Method
    def changePrice(self, new_price):
        self.price = new_price

    def shallow_copy(self):
        return copy.copy(self)
    
    def deep_copy(self):
        return copy.deepcopy(self)


carA = Car("AUDI", "Black", [100, 120, 140])
carB = Car("BMW", "White", [125])
print(carA.color)
print(carB.price)

carC = carA.shallow_copy()
print(carC.name)
carA.price.append(180)
print(carA.price)
print(carC.price)
carB.color_love()
carB.color_love("Blue")
print(carA + " 100")

carB.ride_or_die = False
print(carB.ride_or_die)