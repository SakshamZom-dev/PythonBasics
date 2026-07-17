f = open("file.txt", "r")
data = f.read()
print(data)
f.close()

# # .........................................................


# f1 = open("file1.txt")

# # lines = f1.readlines()
# # print(lines)

# line1 = f1.readline()
# print(line1)
# line2 = f1.readline()
# print(line2)
# line3 = f1.readline()
# print(line3)
# line4 = f1.readline()
# print(line4)
# line5 = f1.readline()           # Returns blank since there is nothing else after line 4 in the text file
# print(line5)


# f1.close()

# # .........................................................

# f1 = open("file1.txt")

# line = f1.readline()
# while(line != ""):
#     print(line)
#     line = f1.readline()

# f1.close()

# # .........................................................

# agree = "Yes, so you just have to do scooby doo bee do"

# f2 = open("file2.txt", "a")
# f2.write(agree)

# f2.close()