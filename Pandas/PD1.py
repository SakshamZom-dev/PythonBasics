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

print(df)

print(df.shape)         # Identifies shape
print(df.head())        # Returns first 5 coulumns
print(df.tail())        # Returns last 5 coulmuns
print(df.info())        # column names, types, null counts
print(df.describe())    # stats for numeric columns
print(df.columns)       # list of column names

# # .........................................................