import pandas as pd

df = pd.DataFrame({
    "name": ["Rio", "Gem", "Sam", "Ana", "Ben", "Eli", "Mia", "Leo", "Ava", "Noah"],
    "marks": [47, 31, 55, 62, 38, 71, 44, 89, 52, 67],
    "subject": ["CDS", "CSE", "Math", "Phy", "CSE", "CDS", "Chem", "Bio", "Eng", "Math"]
})

# # .........................................................

# print(df["marks"])                  # Single column : returns Series
# print(df["name"])

# print(df[["name", "marks"]])        # Multiple columns : returns DataFrame

# # .........................................................

# # Rows by index number
# print(df.iloc[0])                   # first row
# print(df.iloc[0:3])                 # first 3 rows

# # Rows by label/condition
# print(df.loc[df["marks"] > 60])
# print(df.loc[df["subject"] == "CSE"])

# # .........................................................

print(df[df["marks"] < 60]["marks"])                # Chained Brackets
# OR
print(df.loc[df["marks"] < 60, "marks"])            # df.loc is way more efficient

print(df[df["marks"] < 60])                         # Chained Brackets
# OR
print(df.loc[df["marks"] < 60])                     # df.loc is way more efficient