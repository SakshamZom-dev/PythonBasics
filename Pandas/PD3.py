import pandas as pd

# # .........................................................

# df = pd.DataFrame({
#     "name":   ["Zom", "Alex", "Rio"],
#     "marks":  [85, 72, 40],
#     "branch": ["CSE", "ECE", "CSE"]
# })
# print(df)

# # New column
# df["grade"] = ["A", "B", "C"]
# print(df)

# # Computed column
# df["passed"]  = df["marks"] >= 60           # True / False coulumn
# print(df)

# # Modify existing
# df["marks"] = df["marks"] * 1.1             # 10% Bonus
# print(df)

# # .........................................................

# Database with some missing values for practice
df = pd.DataFrame({
    "name": ["Rio", "Gem", "Sam", "Ana", "Ben", "Eli", "Mia", "Leo", "Ava", "Noah"],
    "marks": [47, None, 55, 62, 38, None, 44, 89, 52, 67],
    "subject": ["CDS", "CSE", None, "Phy", "CSE", "CDS", "Chem", "Bio", None, "Math"]
})

# Handling missing values
print(df.isnull().sum())                        # count missing per column

df1 = df.dropna()                               # drop rows with any missing value
print(df1)

df2 = df.fillna(0)                              # fill missing with 0
print(df2)

df3 = df.copy()                                 # fill with column average
df3["marks"] = df3["marks"].fillna(df3["marks"].mean())
print(df3)