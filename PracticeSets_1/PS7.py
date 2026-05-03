import pandas as pd

data = {
    "name":    ["Zom", "Alex", "Rio", "Gemi", "Max", "Sam"],
    "marks":   [85, 72, None, 90, 58, 76],
    "branch":  ["CSE", "ECE", "CSE", "AIML", "ECE", "CSE"],
    "year":    [2, 3, 2, 1, 3, 2]
}

df = pd.DataFrame(data)


# Tasks:

# 1. Print shape and column names

print(df.shape)
print(df.columns)

# 2. Show first 3 rows

print(df.iloc[0 : 3])

# 3. Fill missing marks with the column mean (round to 2 decimal)

df["marks"] =  df["marks"].fillna(round(df["marks"].mean(), 2))

# 4. Filter: only CSE students

print(df.loc[df["branch"] == "CSE"])

# 5. Filter: students with marks >= 75

print(df.loc[df["marks"] >= 75])

# 6. Add a new column "passed" → True if marks >= 60

df["passed"] = df["marks"] >= 60
print(df)

# 7. Show only name and marks of students who passed

print(df.loc[df["passed"], ["name", "marks"]])
# OR
print(df[df["passed"]][["name","marks"]])