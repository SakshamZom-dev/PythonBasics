import numpy as np

# # .........................................................

# Python list "math"
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)        # concatenation, not math
print(a * 2)        # repeats, not multiply

# # NumPy fixes this
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)        # actual math
print(a * 2)        # element-wise

# # Also NumPy is 50-100x faster than lists for large data

# # ...(numpy method of addition, works on both, np_array and lists too)...
c = np.add(a, b)
print(f"a+b (numpy method) = {c}")

# # .........................................................

# From a list
a = np.array([12,13,14,15])
b = np.array([23,24,25,26])
print(a)
print(b)

# Ranges
c = np.arange(0, 101, 10)   # (start, stop, step)
print(c)
d = np.linspace(0, 1, 5)    # 5 evenly spaced
print(d)

# Preset arrays
zeroes = np.zeros(5)
print(zeroes)
ones = np.ones(5)
print(ones)

zeroes1 = np.zeros((2, 3))      # 2 rows, 3 columns
print(zeroes1)

sevens = np.full(10, 7)         # 10 times 7 
print(sevens)

sevens1 = np.full((2, 3), 7)    # 2 rows, 3 columns of 7
print(sevens1)


print(a.size)               # Total Elements
print(a.ndim)               # No. of dimentions
print(a.shape)              # Size of dimentions
print(a.dtype)              # Type of Data
# # .........................................................