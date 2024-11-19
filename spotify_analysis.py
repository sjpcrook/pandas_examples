import pandas as pd

df = pd.read_csv("spotify_songs.csv")
# print(df)

# print(df.shape)

# print(df["playlist_genre"].value_counts())

# print(df["playlist_genre"].mode()) #*Returns a series
# print(df["playlist_genre"].mode()[0]) #*Returns an object

# print(df["duration_ms"].median()) #*Returns a float
# print(df["duration_ms"].mean()) #*Returns a float

# min_ms = df["duration_ms"].min()
# print(min_ms)
# max_ms = df["duration_ms"].max() 
# print(max_ms)
# range_ms = max_ms - min_ms
# print(range_ms) 

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"], ascending=False))

# print(df.groupby("playlist_genre")["duration_ms"].max())

# print(df.query("track_artist == 'Ricky Martin'"))

mean_ms = df["duration_ms"].mean()
print(mean_ms)
print(df.query("duration_ms >= @mean_ms"))


