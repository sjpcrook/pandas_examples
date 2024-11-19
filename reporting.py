import pandas as pd
import sweetviz as sv

# resultsdf = pd.read_csv("results.csv")
# resultsreport = sv.analyze(resultsdf)
# resultsreport.show_html()

# shootoutsdf = pd.read_csv("shootouts.csv")
# shootoutsreport = sv.analyze(shootoutsdf)
# shootoutsreport.show_html()

# scorersdf = pd.read_csv("goalscorers.csv")
# scorersreport = sv.analyze(scorersdf)
# scorersreport.show_html()

# spotifydf = pd.read_csv("spotify_songs.csv")
# spotifyreport = sv.analyze(spotifydf)
# spotifyreport.show_html()

planetdf = pd.read_excel("planet_facts.xlsx")
planetreport = sv.analyze(planetdf)
planetreport.show_html()