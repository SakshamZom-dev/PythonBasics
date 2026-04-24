# # Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Zom", 5000)
print(acc.get_balance())

acc.deposit(2000)
print(acc.get_balance())

acc.withdraw(1000)
print(acc.get_balance())

# can't touch private attribute directly
# print(acc.__balance)     # AttributeError