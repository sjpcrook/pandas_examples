
#*---- Activity 1 -------------------------------------------------

import pandas as pd

df = pd.read_csv("results.csv")

# print(df.info())

#*How many different kinds of tournaments were played?

# print(len(df["tournament"].value_counts()))

#*How many matches were played under each tournament?

# print(df["tournament"].value_counts())

#*Most reported home team?

# print(df["home_team"].mode()[0])

#*Most reported away team?

# print(df["away_team"].mode()[0])

#*Least reported home team?

# print(df["home_team"].value_counts().index[-1])

#*Least reported away team?

# print(df["away_team"].value_counts().index[-1])




#*---- Activity 2 -------------------------------------------------

#*How many time England played at home in each tournament?

eng_home_df = df.query("home_team == 'England'") #*Used in later answers
# print(eng_home_df)


# print(eng_home_df["tournament"].value_counts())


#*How many times England scored more than the average amount of goals at a home match?

home_mean = df["home_score"].mean()
eng_home_more_df = eng_home_df.query("home_score > @home_mean")

# print(eng_home_more_df.shape[0])

#*How many times England scored more than the average amount of goals at a home match?

eng_away_df = df.query("away_team == 'England'")
away_mean = df["away_score"].mean()
eng_away_more_df = eng_away_df.query("away_score > @away_mean")

# print(eng_away_more_df.shape[0])

#*What is England's average number of goals scored at home?

# print(eng_home_df["home_score"].mean())

#*What is each team's average home and away score?

home_teams = df["home_team"].unique()
home_av_scores = {}
for team in home_teams:
    home_av_scores[team] = df.query("home_team == @team")["home_score"].mean()
home_av_df = pd.DataFrame.from_dict(home_av_scores, orient="index", columns=["Average Home Score"])
# print(home_av_df)
print(home_av_df.loc["Iceland"])


away_teams = df["away_team"].unique()
away_av_scores = {}
for team in away_teams:
    away_av_scores[team] = df.query("away_team == @team")["away_score"].mean()
away_av_df = pd.DataFrame.from_dict(away_av_scores, orient="index", columns=["Average Away Score"])
# print(away_av_df)
# print(away_av_df.loc["Spain"])

