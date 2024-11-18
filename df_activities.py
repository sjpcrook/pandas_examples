import pandas as pd

names = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
temps = pd.Series([67, 464, 15, -60, -108, -139, -197, -201])
radii = pd.Series([2439.7, 6051.8, 6371.0, 3389.5, 69911, 58232, 25362, 24622])
colours = pd.Series(["Grey", "Yellow", "Blue and Green", "Red", "Brown", "Brown", "Cyan", "Blue"])
features = pd.Series(["Craters and plains", "Spins Backwards", "Has life", "Desert Planet","90% Hydrogen", "Rings", "Spins on its side", "Storms"])
df = pd.concat([names, temps, radii, colours, features], axis = 1)
df.columns = ["Planet", "Av. Temperature (C)", "Radius (km)", "Colour", "Features"]
#print(df)
discoverers = pd.Series(["Galileo", "Galileo", "Earliest Humans", "Galileo", "Galileo", "Galileo", "Herschel", "Gottfried Galle"])
year = pd.Series([1610, 1610, "300,000 BC", 1610, 1610, 1610, 1781, 1846])
composition = pd.Series(["Oxygen", "Carbon Dioxide", "Nitrogen", "Carbon Dioxide", "Hydrogen", "Hydrogen", "Hydrogen", "Hydrogen"])
df = pd.concat([df, discoverers, year, composition], axis = 1)
df.rename(columns={0:"Discoverers", 1:"Year of Discovery", 2:"Composition"}, inplace=True)
df.loc[8] = ["Pluto", -229, 2376.6, "White", "Dwarf Planet", "Tombaugh", 1930, "Nitrogen"]
print(df)
#df.to_excel("planet_facts.xlsx")