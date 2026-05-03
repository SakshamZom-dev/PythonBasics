import pandas as pd

df = pd.DataFrame({
    "name": ["Rio", "Gem", "Sam", "Ana", "Ben", "Eli", "Mia", "Leo", "Ava", "Noah"],
    "marks": [47, None, 55, 62, 38, None, 44, 89, 52, 67],
    "subject": ["CDS", "CSE", None, "Phy", "CSE", "CDS", "Chem", "Bio", None, "Math"]
})

# print(df)

# print(df.isnull().sum())

# df1 = df.dropna()
# print(df1)

# df2 = df.fillna("<Error>")
# print(df2)

# df3 = df.copy()
# df3["marks"] = df["marks"].fillna("<ABSENT>")
# print(df3)

# df4 = df.copy()
# df4["marks"] = df4["marks"].fillna(df4["marks"].mean())
# print(df4)

# print([df.shape, df.columns])

# df["Activity_Grades"] = ["A", "B", None, None, "C", "A", None, "A", None, None]
# print(df)

# df["passed"]  = df["marks"] >= 60
# print(df)

# print(df["marks"].min())


# print(df[df["marks"] < 60]["marks"])
# # OR
# print(df.loc[df["marks"] < 60, "marks"])

# print(df[df["marks"] < 60])
# # OR
# print(df.loc[df["marks"] < 60])