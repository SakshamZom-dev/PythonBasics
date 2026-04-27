import numpy as np

# # .........................................................

# marks = np.array([85, 72, 90, 68, 95, 78])


# print(np.sum(marks))

# print(np.mean(marks))
# print(np.median(marks))
# print(np.std(marks))            # standard deviation

# print(np.max(marks))
# print(np.min(marks))
# print(np.argmax(marks))         # INDEX of max value
# print(np.argmin(marks))         # INDEX of min value


# # Boolean Indexing — Filter without loops
# print(marks > 80)
# print(marks[marks > 80])
# print(marks[(marks > 70) & (marks < 90)])
# print(marks[(marks < 70) | (marks > 90)])

# # .........................................................

# # Reshape — Change array dimensions

# a = np.arange(1, 10)
# print(a)

# b = a.reshape(3,3)              # Convert to 3x3
# print(b)

# # Rule: rows × cols must equal original size

# # .........................................................

marks = np.array([
    [85, 90, 78],
    [72, 88, 95],
    [90, 76, 83]
])

print(np.sum(marks, axis = 0))      # sum DOWN each column (Vertically)
print(np.sum(marks, axis = 1))      # sum ACROSS each row (Horizontally)