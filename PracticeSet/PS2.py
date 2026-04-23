# Create a class called Phone with:
# - brand, model, price as attributes
# - a method called info() that prints:
#   "Brand: X | Model: Y | Price: ₹Z"

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def info(self):
        print(f"Hello, this is {self.brand} {self.model}, with the listed price of ₹{self.price}")

# Then create 2 objects and call info() on both

a = Phone("Apple", "iPhone 17", 100000)
b = Phone("CMF by Nothing", "2 Pro", 20000)

a.info()
b.info()