import numpy as np

# Python list "math"
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)        # [1, 2, 3, 4, 5, 6]  ← concatenation, not math
print(a * 2)        # [1, 2, 3, 1, 2, 3]  ← repeats, not multiply

# NumPy fixes this
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)        # [5, 7, 9]  ← actual math
print(a * 2)        # [2, 4, 6]  ← element-wise

# Also NumPy is 50-100x faster than lists for large data