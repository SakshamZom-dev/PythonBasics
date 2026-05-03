import pandas as pd

data = {
    "title":  ["Inception", "Avatar", "Joker", "Titanic", "Parasite", "Interstellar", "Frozen"],
    "genre":  ["Sci-Fi", "Sci-Fi", "Drama", "Drama", "Drama", "Sci-Fi", "Animation"],
    "rating": [8.8, 7.9, 8.5, 7.8, 8.6, 8.6, 7.4],
    "year":   [2010, 2009, 2019, 1997, 2019, 2014, 2013],
    "gross_m":[292, 2847, 1079, 2187, 258, 701, 1280]
}

df = pd.DataFrame(data)

# # .........................................................

# # Sorting
# print(df.sort_values("rating", ascending= False))
# print(df.sort_values(["genre", "rating"], ascending = [True, False]))

# # Frequency of each category
# print(df.groupby("genre") ["title"].count())
# print(df["genre"].value_counts())

# # .........................................................

# # Remove rows or columns
# df1 =df.drop(columns= ["year"])                         # Drop a column
# print(df1)                                              # drop() doesn't modify original by default — it returns a new DataFrame

# df2 = df.drop(columns= ["year", "gross_m"])             # Drop multiple columns
# print(df2)

# df3 = df.drop(index= 0)                                 # Drop a row by index number
# print(df3)

# lowRated = df[df["rating"] < 8.0].index                   # Drop rows by condition
# df4 = df.drop(index=lowRated)
# print(df4)
# # # OR
# # lowRated = df.loc[df["rating"] < 8.0].index             # First prior, consistent (as .loc is there)

# # .........................................................

# # Use inplace=True when we have to change the orignal dataframe
# df.drop(columns=["gross_m"], inplace= True)
# print(df)

# # .........................................................

# Apply a custom function to a column

df["rating_percent"] = df["rating"].apply(lambda x : x * 10)            # Simple lambda
print(df)


def grade(rating):                                                      # Custom function
    if rating >= 8.5:
        return "A"
    elif rating >= 8.0:
        return "B"
    else:
        return "C"
df["grade"] = df["rating"].apply(grade)
print(df)