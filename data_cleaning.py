import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

# print(df)

# print(df.describe())

# df.info()

df = df.set_index("Transaction ID")

df = df.drop(columns=["Till ID", "Unnamed: 0"])
#* OR
# df = df.drop("Till ID", axis = 1)

df = df.dropna(how = "any")

# print(df[df.duplicated()])
df = df.drop_duplicates()
# print(df[df.duplicated()])

df.at[15.0, "Cost"] = 6.00

def float_to_time(time_record):
    time_record = str(time_record)
    hours, minutes = time_record.split(".")
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)
df["Time"] = pd.to_datetime(df["Time"])
# print(df)

def str_to_list(basket_list):
    basket_list = basket_list.split(", ")
    return(basket_list)

df["Basket"] = df["Basket"].apply(str_to_list)

exploded_df = df.explode("Basket")

print(exploded_df["Basket"].value_counts())