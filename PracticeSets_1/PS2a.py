# # Inheritance

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def specs(self):
        print(f"Hello, this is {self.brand} {self.model}, with the listed price of ₹{self.price}")
    def call(self):
        print(f"{self.model} is making a call")

class Smartphone(Phone):
    def __init__(self, brand, model, price, os, ram):
        super().__init__(brand, model, price)
        self.os = os
        self.ram = ram
    def app_info(self):
        print(f"Runs {self.os} with {self.ram}GB RAM")

a = Smartphone("Apple", "iPhone17", 100000, "iOS", 8)
a.specs()
a.call()
a.app_info()