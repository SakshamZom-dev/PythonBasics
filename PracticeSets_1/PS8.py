import pandas as pd

data = {
    "title":  ["Inception", "Avatar", "Joker", "Titanic", "Parasite", "Interstellar", "Frozen"],
    "genre":  ["Sci-Fi", "Sci-Fi", "Drama", "Drama", "Drama", "Sci-Fi", "Animation"],
    "rating": [8.8, 7.9, 8.5, 7.8, 8.6, 8.6, 7.4],
    "year":   [2010, 2009, 2019, 1997, 2019, 2014, 2013],
    "gross_m":[292, 2847, 1079, 2187, 258, 701, 1280]  # revenue in millions
}

df = pd.DataFrame(data)

# 1. Basic info — shape, columns, describe()

print(df.shape)
print(df.columns)
print(df.describe())

# 2. Highest rated movie (use idxmax())

print(df["rating"].max())                           # Just the value of rating

max_rating = df["rating"].idxmax()
print(df.loc[max_rating, "title"])                  # Will return the movie whose rating is higher(as per the question)

# 3. All movies with rating >= 8.5

print(df.loc[df["rating"] >= 8.5, ["title", "rating"]])

# 4. Average rating per genre".

print(df.groupby("genre") ["rating"].mean())

# 5. Total gross revenue per genre

print(f"The total gross revenue per genre:\n{df.groupby('genre')['gross_m'].sum()}")

# 6. Add column "blockbuster" → True if gross_m > 1000

df["blockbuster"] = df["gross_m"] > 1000
print(df)

# 7. Which genre has the most blockbusters? (groupby + sum on blockbuster column)

blockbuster_counts = df.groupby("genre") ["blockbuster"].sum()
print(blockbuster_counts.idxmax())