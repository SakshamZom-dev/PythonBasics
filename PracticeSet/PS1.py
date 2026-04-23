raw_scores = [85, 92, 85, 78, 92, 88, 78]

# 1. Find unique scores (use a set)
unique_scores = set(raw_scores)
print(unique_scores)

# 2. Sort them in ascending order (convert to list, then sort)
sorted_scores = sorted(list(raw_scores))
print(sorted_scores)

# 3. Store top score with student name in a dict
topper_record = {"name" : "Zom", "score" : sorted_scores[-1]}
print(topper_record)

# 4. Return top 3 scores as a tuple (immutable record)
top_3_tuple = tuple(sorted_scores[-3:])
print(top_3_tuple)