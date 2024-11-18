import pandas as pd

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])

# # print(languages)

# rankings = pd.Series([3, 1, 2, 4])

# # print(rankings)

# # df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)], columns=["Name", "Age"])

# # print(df)

# # df = pd.DataFrame({
# #     "Languages": languages,
# #     "Ranking": rankings
# # })
# # print(df)

# df2 = pd.concat([languages, rankings], axis = 1)
# df2.columns = ["Languages", "Ranking"]
# print(df2)

# df = pd.read_csv("speeds.csv")
# print(df)

df = pd.read_excel("speeds.xlsx")

print(df)