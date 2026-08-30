print("My age is", 19)
print('I am 19')

a = 10
print (a)
print(type(a))

name = "Saksham"
print(name)
print(type(name))

b = 12.34
print(b)
print(type(b))
c = str(b)
print(c)
print(type(c))

pi = 3.14
print (pi)
print(type(pi))
print(int(pi))

isOk = True
print (isOk)
print(type(isOk))
print(str(isOk))
print(int(isOk))

# # .........................................................

# a = "Python SMART file"
# print(a.upper())
# print(a.lower())
# print(a[0])
# print(a[7])
# print(a[2:9])

# # .........................................................

# # Seperator and end usage
# print("Yo", "hello", "How's going", "What's up?", sep="( ! )", end=" ($)\n")

# # .........................................................

# # Arithmatic Operators
# a = 10
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)

# print(a / b)
# print(f"{a / b:.2f}")             # upto two decimal places

# print(a // b)
# print(a % b)
# print(a ** b)

# # .........................................................

# # Comparison Operators
# a = 5
# b = 10
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= b)
# print(a < b)
# print(a <= b)

# # .........................................................

# # Logical Operators
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)

# # .........................................................

# # Assignment Operators
# a = 5
# print(f"Orignal value is: {a}")
# a += 2
# print(a)
# a -= 6
# print(a)
# a *= 20
# print(a)
# a /= 2
# print(a)

# # .........................................................

# # Identity & Membership (Python‑only concepts)
# listA = [12, 23, 34, 45]
# listB = [13, 43, 76, 12]
# listC = [12, 23, 34, 45]

# print(listA is listB)
# print(listA is listC)
# print(12 in listA)
# print(77 in listA)

# # .........................................................

# newName = input("Write your name:\t")
# age = int(input("Enter your age plzz:\t"))

# if age >= 18:
#     if age >= 70:
#         print("Legend Spotted!")
#     else:
#         print("Damn! Citizen Spotted")
#     print("You can definately vote")
# elif age < 0:
#     print("Are you kidding me?")
#     exit()
# else:
#     print("Get out of here!")
#     exit()

# condition = input(f"\nHello {newName}, How's it going? (good/bad) ").lower()
# if condition == 'good':
#     print("That's the spirit!")
# elif condition == 'bad':
#     print("WTH!")
# else:
#     print("Input somethin valid broo")

# # .........................................................

# a = int(input("Enter the first one:\t"))
# b = int(input("Enter the second one:\t"))
# c = int(input("Enter the third one:\t"))

# if a == b and a == c:
#     print("All are equal bro")
# elif a >= b and a >= c:
#     print(f"Clearly,{a} is greatest here")
# elif b >= a and b >= c:
#     print(f"Surely, {b} is the greatest one")
# else:
#     print(f"{c} is the greatest number here")

# # .........................................................

# for i in range(5):
#     print(i)

# i = 0
# while(i < 5):
#     print(i)
#     i += 1

# for i in range(1, 6):
#     print(i)

# i = 1
# while(i < 6):
#     print(i)
#     i += 1

# students = ["Zom", "Alex", "Rio", "Gemi"]
# for stud in students:
#     print(stud)

# i = 0
# while i < 3:
#     print("Count: ", i)
#     i += 1

# fruits = ["apple", "banana", "cherry"]
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# for i in range(3):
#     for j in range(2):
#         print(i, j)


# # .........................................................

# [print (i) for i in range(1, 6)]

# i = 0
# while i < 3 : print(i) ; i += 1

# [print(fruit) for fruit in ["apple", "banana", "cherry"]]

# [print(i, j) for i in range(3) for j in range(2)]

# # .........................................................

# for i in range(20):
#     if i == 8:
#         break   # Stop at 8
#     if i % 2 == 0:
#         print(i)

# for i in range(20):
#     if i == 8:
#         continue    # Skip 8
#     if i % 2 == 0:
#         print(i)