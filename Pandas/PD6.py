import pandas as pd

# # .........................................................

movies = pd.DataFrame({
    "title":  ["Inception", "Avatar", "Joker"],
    "genre":  ["Sci-Fi", "Sci-Fi", "Drama"],
    "rating": [8.8, 7.9, 8.5]
})

box_office = pd.DataFrame({
    "title":   ["Inception", "Avatar", "Titanic"],
    "gross_m": [292, 2847, 2187]
})


# how="inner"  : only rows that exist in BOTH
merged1 = pd.merge(movies, box_office, on= "title", how= "inner")
print(merged1)

# how="outer"  : all rows from both, NaN where no match
merged2 = pd.merge(movies, box_office, on= "title", how="outer")
print(merged2)

# how="left"   : all rows from left df, NaN if no match in right
merged3 = pd.merge(movies, box_office, on= "title", how="left")
print(merged3)

# how="right"  : all rows from right df
merged4 = pd.merge(movies, box_office, on= "title", how="right")
print(merged4)

# # .........................................................

# data = {
#     "title":  ["Inception", "Avatar", "Joker", "Titanic", "Parasite", "Interstellar", "Frozen"],
#     "genre":  ["Sci-Fi", "Sci-Fi", "Drama", "Drama", "Drama", "Sci-Fi", "Animation"],
#     "rating": [8.8, 7.9, 8.5, 7.8, 8.6, 8.6, 7.4],
#     "gross_m":[292, 2847, 1079, 2187, 258, 701, 1280]
# }
# df = pd.DataFrame(data)


# # Excel-style pivot (Kinda feel like groupby, but is more professional)
# pivot = df.pivot_table(
#     values= "rating",
#     index= "genre",
#     aggfunc= "mean"
# )

# print(pivot)

# # .........................................................

# df = pd.DataFrame({
#     "title": ["inception", "AVATAR", "Joker "],
#     "genre": ["sci-fi", "sci-fi", "drama"]
# })


# # String Operations

# df["title"] = df["title"].str.title()                       # Title Case
# print(df)

# df["title"] = df["title"].str.upper()                       # UpperCase
# print(df)

# df["title"] = df["title"].str.strip()                       # Remove whitespace
# print(df)

# print(df.loc[df["title"].str.contains("Jo")])               # Contains — like search

# df["genre"] = df["genre"].str.replace("-", " ")             # Replace
# print(df)

# df["title_length"] = df["title"].str.len()                  # Length column
# print(df)