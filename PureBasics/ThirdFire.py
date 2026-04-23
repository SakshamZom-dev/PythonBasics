# # Adding somethinhg in the string
stringa = "abcdefg"
stringa = stringa[:2] + 'x' + stringa[2:]
print(stringa)  # abxcdefg

# # .........................................................

# # Replacing something in a string
stringa = "abcdefg"
stringa = stringa[:2] + 'x' + stringa[3:]
print(stringa)  # abxdefg

# # .........................................................

batch = "There are 5 girls and 4 boys in the class"
new1 = batch[8:]
print(new1)
new2 = batch[:13]
print(new2)
new3 = batch[9:12]
print(new3)
new4 = batch[-4:]
print(new4)
new5 = batch[3:14:2]
print(new5)

# # .........................................................

Greet = "Hi John, I hope you're good today"
print("John" in Greet)
print("Adam" in Greet)
print("Adam" not in Greet)

# # .........................................................

stringa = "abcd"
stringb = "efgh"
stringc = "abgh"
x1 = (stringa * 2)
print(x1)
x2 = (stringa + stringb)
print(x2)

# # .........................................................

