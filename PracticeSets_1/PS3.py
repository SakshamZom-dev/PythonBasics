# Parent: Vehicle
#   attributes: brand, speed (km/h)
#   method: describe() → "Brand: X | Top Speed: Y km/h"

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    def describe(self):
        print(f"Brand: {self.brand} | Top Speed: {self.speed} km/h")

# Child: ElectricVehicle (inherits Vehicle)
#   extra attributes: battery_capacity (kWh)
#   method: ev_info() → "Battery: Z kWh"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
    def ev_info(self):
        print(f"Battery: {self.battery_capacity} kWh")

#   override describe() → add "[EV]" tag at the start
    def describe(self):
        print(f"EV Brand: {self.brand} | Top Speed: {self.speed} km/h")

# Create one Vehicle and one ElectricVehicle, call all methods

a = Vehicle("Land Rover Defender", 210)
b = ElectricVehicle("Mahindra BE6E", 160, 100)

a.describe()
b.describe()
b.ev_info()