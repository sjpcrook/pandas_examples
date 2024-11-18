import pandas as pd

df = pd.read_excel("dev_rankings.xlsx")

#print(df)

df = df.set_index("Languages")
# print(df)

# print(df["Ranking 2019"])
# print(df[["Ranking 2022", "Ranking 2021"]])

# print(df.loc["HTML"])
# print(df.loc[:, "Ranking 2020"])

# print(df.loc["Python":"HTML":1, "Ranking 2023"::2])
# print(df.iloc[0:3:1, 0::2])
# print(df.at(["HTML", "Ranking 2023"]))

print(df.head(2))