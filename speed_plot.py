import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("results2024-11-25-1432.xlsx")

plt.style.use("ggplot")

# df2 = df.drop(columns = ["Unnamed: 0", "Date-time"])
# plt.ylabel("Speed (Mb/s)")
# df2.boxplot()
# plt.show()

pd.DataFrame(df["Download (Mb/s)"]).boxplot()
plt.ylabel("Download Speed (Mb/s)")
plt.show()

pd.DataFrame(df["Upload (Mb/s)"]).boxplot()
plt.ylabel("Upload Speed (Mb/s)")
plt.show()

plt.plot(df["Unnamed: 0"]*60*20, df["Download (Mb/s)"], label = "Download Speed", color="red")
plt.plot(df["Unnamed: 0"]*60*20, df["Upload (Mb/s)"], label = "Upload Speed", color="blue", linestyle = "dashed")

plt.title("Internet Speed over Time")
plt.xlabel("Time (s)")
plt.ylabel("Speed (Mb/s)")
plt.legend()
plt.show()

