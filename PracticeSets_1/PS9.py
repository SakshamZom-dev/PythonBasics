import pandas as pd

data = {
    "title":  ["Inception", "Avatar", "Joker", "Titanic", "Parasite", "Interstellar", "Frozen"],
    "genre":  ["Sci-Fi", "Sci-Fi", "Drama", "Drama", "Drama", "Sci-Fi", "Animation"],
    "rating": [8.8, 7.9, 8.5, 7.8, 8.6, 8.6, 7.4],
    "year":   [2010, 2009, 2019, 1997, 2019, 2014, 2013],
    "gross_m":[292, 2847, 1079, 2187, 258, 701, 1280]  # revenue in millions
}

df = pd.DataFrame(data)


# 1. Sort by gross_m, highest first — show title and gross_m only

print(df[["title", "gross_m"]].sort_values("gross_m", ascending=False))

# 2. How many movies per genre? (value_counts)

print(df["genre"].value_counts())

# 3. Drop the "year" column, confirm it's gone with df.columns

df.drop(columns= ["year"], inplace= True)
print(df.columns)

# 4. Add a "label" column using apply:
#      gross_m > 1000 → "Blockbuster"
#      gross_m > 500  → "Hit"
#      else           → "Average"

def label(gross_m):
    if gross_m > 1000:
        return "Blockbuster"
    elif gross_m > 500:
        return "Hit"
    else:
        return "Average"

df["label"] = df["gross_m"].apply(label)
print(df)

# # OR
# df["label"] = df["gross_m"].apply(lambda x: "Blockbuster" if x > 1000 else ("Hit" if x > 500 else "Average"))

# 5. Sort by label A-Z, then gross_m highest first

print(df.sort_values(["label", "gross_m"], ascending= [True, False]))