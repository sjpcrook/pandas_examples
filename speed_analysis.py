import pandas as pd
import sweetviz as sv


#* Extracting the information for my personal results, I realise I could have just used .describe()
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


#* Extracting the information on group results, I did calculations for the upper/lower bound by hand using the info found
df = pd.read_excel("group_results.xlsx")

print("Information with outliers:")
print(df.describe())

df.rename(columns={"Mean Download":"Mean_Download"}, inplace=True) 

df = df.query("Mean_Download < 146.60") #*Excludes outliers. Since internet speed cannot be <0, we only worry about the upper bound.
#*I did the calculation by hand so this code isn't very reusable. If I was to do this again, I would write code to find the upper/lower bounds for any given dataset.
#*This way, if we were to add more datapoints, the outliers would still be correct.

print("Information without outliers:")
print(df.describe())

# myreport = sv.analyze(df) #*This does not really provide much useful information
# myreport.show_html()