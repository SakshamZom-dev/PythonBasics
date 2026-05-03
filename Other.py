import pandas as pd

df = pd.DataFrame({
    "name": ["Rio", "Gem", "Sam", "Ana", "Ben", "Eli", "Mia", "Leo", "Ava", "Noah"],
    "marks": [47, 31, 55, 62, 38, 71, 44, 89, 52, 67],
    "subject": ["CDS", "CSE", "Math", "Phy", "CSE", "CDS", "Chem", "Bio", "Eng", "Math"]
})

df["grade"] = pd.cut(df["marks"], 
    bins=[0, 40, 50, 60, 70, 80, 100], 
    labels=["F", "D", "C", "B", "A", "A+"], 
    right=False)
print(df)