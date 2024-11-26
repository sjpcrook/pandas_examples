import pandas as pd

# df = pd.read_excel("results2024-11-25-1432.xlsx")

# min_dl = df["Download (Mb/s)"].min()
# max_dl = df["Download (Mb/s)"].max()
# min_ul = df["Upload (Mb/s)"].min()
# max_ul = df["Upload (Mb/s)"].max()

# mean_dl = df["Download (Mb/s)"].mean()
# median_dl = df["Download (Mb/s)"].median()
# mean_ul = df["Upload (Mb/s)"].mean()
# median_ul = df["Upload (Mb/s)"].median()

# print(max_dl, min_dl, mean_dl, median_dl, max_ul, min_ul, mean_ul, median_ul)

df = pd.read_excel("group_results.xlsx")

print(df.describe())

df.rename(columns={"Mean Download":"Mean_Download"}, inplace=True)
df = df.query("Mean_Download < 146.60")

print(df.describe())