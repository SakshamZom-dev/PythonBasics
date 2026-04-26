import numpy as np

marks = np.array([
    [85, 90, 78],   # Student 1: OS, TOC, Cloud
    [72, 88, 95],   # Student 2
    [90, 76, 83]    # Student 3
])

# 1. Print shape

print(marks.shape)

# 2. Get Student 2's TOC mark (row 1, col 1)

print(marks[1,1])

# 3. Get all students' Cloud marks (all rows, col 2)

print(marks[: ,2])

# 4. Get top-left 2x2 block

print(marks[0:2, 0:2])

# 5. Multiply all marks by 1.1 (10% bonus) — one line

print(marks[0:3, 0:3] * 1.1)

# Or

print(marks * 1.1)   # cleaner