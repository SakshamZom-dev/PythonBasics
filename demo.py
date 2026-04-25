import numpy as np

# From a list
a = np.array([12,13,14,15])
b = np.array([23,24,25,26])
print(a)
print(b)

# Ranges
c = np.arange(0, 101, 10)   # [0, 2, 4, 6, 8]  (start, stop, step)
print(c)
d = np.linspace(0, 1, 5)    # [0, 0.25, 0.5, 0.75, 1.0] — 5 evenly spaced
print(d)

# Preset arrays
zeroes = np.zeros(5)
print(zeroes)
ones = np.ones(5)
print(ones)

sevens = np.full(7, 10)
print(sevens)