import pandas as pd

students = pd.DataFrame({
    "name":   ["zom", "ALEX", "Rio ", "gemi"],
    "branch": ["cse", "ece", "cse", "aiml"],
    "marks":  [85, 72, 90, 88]
})

scores = pd.DataFrame({
    "name":     ["Zom", "Alex", "Rio", "Max"],
    "projects": [3, 1, 4, 2]
})


# 1. Clean "name" column → Title Case + strip whitespace

students["name"] = students["name"].str.title()
students["name"] = students["name"].str.strip()
print(students)

# 2. Clean "branch" column → UPPERCASE

students["branch"] = students["branch"].str.upper()
print(students)

# 3. Merge students with scores on "name" (left join)

merged = pd.merge(students, scores, on= "name", how= "left")
print(merged)

# 4. Create a pivot_table: average marks per branch

avg_pivot = students.pivot_table(
    values= "marks",
    index= "branch",
    aggfunc= "mean"
)
print(avg_pivot)

# 5. Filter: students whose name contains "o" (after cleaning)

print(students.loc[students["name"].str.contains("o")])
# students["name"].str.contains("o", case=False)  # case-insensitive (best way to tacke something which includes O instead of o)