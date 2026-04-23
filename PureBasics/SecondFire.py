# def greet():
#     print("HELLO")

# greet()

# # .........................................................

# def greet1(name):
#     print(f"Hello {name}")

# a = input("Whats your name?\t")
# greet1(a)

# # .........................................................

# def introduce(name, age):
#     print(f"My name is {name} and I am {age} years old.")

# introduce(age=19, name="Saksham")

# # .........................................................

# def greet2(name):
#     return f"Hello, {name}"

# a = input("Whats your name?\t")
# print(greet2(a))

# # .........................................................

# def sq(num, exp = 2):
#     return num ** exp

# print(sq(5))
# print(sq(5,3))

# # .........................................................

# def AddAndMultiply(a, b):
#     Addition = a+b ; Multiplication = a*b
#     return Addition, Multiplication

# print(AddAndMultiply(12,2))

# add, multipy = AddAndMultiply(14, 2)
# print(f"Addition: {add}, Multiplication: {multipy}")

# # .........................................................

def addAll(*nums):
    return sum(nums)

print(f"Addition is: {addAll(12, 10, 13, 23)}")

a = (12, 100, 13, 23)
print(f"New Addition is: {addAll(*a)}")

# # .........................................................

