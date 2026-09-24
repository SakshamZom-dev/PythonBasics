import numpy as np

matrix = np.array([
    [12, 13, 14],
    [15, 16, 17],
    [18, 19, 20]
])

print(matrix)
print(matrix.ndim)
print(matrix.shape)
print(matrix.size)

# Indexing [row, column]
print(matrix[0, 0])
print(matrix[1, 2])
print(matrix[2, -1])

# Slicing
print(matrix[0, :])         # entire first row
print(matrix[: ,0])         # entire first column
print(matrix[0:2 , 0:3])    # 2 rows, 3 columns
print(matrix[0:2, 1:3])     # 2 rows, 1 column

# If your matrix only has 2 columns, but you ask for 0:3, it won't crash. 
# It will simply return all available columns up to the boundary.