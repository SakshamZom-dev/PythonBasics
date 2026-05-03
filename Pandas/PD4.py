import pandas as pd

data = {
    "name":   ["Zom", "Alex", "Rio", "Gemi", "Max", "Sam"],
    "marks":  [85, 72, 81, 90, 58, 76],
    "branch": ["CSE", "ECE", "CSE", "AIML", "ECE", "CSE"]
}

df = pd.DataFrame(data)

print(df["marks"].mean())

print(df.groupby("branch")["marks"].mean())
print(df.groupby("branch")["marks"].max())
print(df.groupby("branch")["marks"].min())
print(df.groupby("branch")["marks"].count())
print(df.groupby("branch")["marks"].agg(["mean", "max", "min", "count"]))