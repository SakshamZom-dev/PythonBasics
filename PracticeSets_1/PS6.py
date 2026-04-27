import numpy as np

scores = np.array([55, 82, 91, 47, 76, 88, 63, 95, 70, 40])

# 1. Mean, max, min

print(np.mean(scores))
print(np.max(scores))
print(np.min(scores))

# 2. Who passed? (score >= 60) — print passing scores

print(scores[scores >= 60])

# 3. How many students passed? (hint: len() or .sum() on boolean)

pass_mark = scores >= 60
print(pass_mark.sum())

# OR

print(len(scores[scores >= 60]))

# 4. Scores of students who scored between 70 and 90 (inclusive)

print(scores[(scores >= 70) & (scores <= 90)])

# 5. Reshape scores into a 2x5 matrix, then find column-wise max (axis=0)

matrix = scores.reshape(2, 5)
print(matrix)

print(np.max(matrix, axis = 0))