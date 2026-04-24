class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(self):
        print("Meow")
class Duck:
    def sound(self):
        print("Quack")

d = Dog(); d.sound()
c = Cat(); c.sound()
dk = Duck(); d.sound()

print("\n")

animals = [Dog(), Cat(), Duck()]
[animal.sound() for animal in animals]