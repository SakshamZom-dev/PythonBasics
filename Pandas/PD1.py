import pandas as pd

# # .........................................................

# s = pd.Series([12, 13,14], index = ["Zom", "Rio", "Gem"])
# print(s)

# # .........................................................

df = pd.DataFrame({
    "name": ["Rio", "Gem", "Sam", "Ana", "Ben", "Eli", "Mia", "Leo", "Ava", "Noah"],
    "marks": [47, 31, 55, 62, 38, 71, 44, 89, 52, 67],
    "subject": ["CDS", "CSE", "Math", "Phy", "CSE", "CDS", "Chem", "Bio", "Eng", "Math"]
})

print(df , "\n")

print(df.shape , "\n")        # Identifies shape
print(df.head(), "\n")        # Returns first 5 rows
print(df.tail(), "\n")        # Returns last 5 rows
print(df.info(), "\n")        # column names, types, null counts
print(df.describe(), "\n")    # stats for numeric columns
print(df.columns, "\n")       # list of column names

# # .........................................................