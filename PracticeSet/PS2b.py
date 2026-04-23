# # Inheritance with overiding

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def specs(self):
        print(f"Hello, this is {self.brand} {self.model}, with the listed price of ₹{self.price}")

class BudgetPhone(Phone):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)
    def specs(self):                                                    # Same name as parent — overrides it
        print(f"[Budget Pick] {self.brand} {self.model} at just ₹{self.price}!")

b = BudgetPhone("CMF", "2 Pro", 20000)
b.specs()