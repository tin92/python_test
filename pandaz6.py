import pandas as pd
import requests
import datetime
import scipy
import random 
from numpy.random import randint
from numpy.random import rand
from datetime import date, timedelta
from io import StringIO
import matplotlib.pyplot as pyplot
import seaborn as sns

link = "http://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

def read_text(web: str):
    respons = requests.get(web)
    data = pd.read_csv(StringIO(respons.text))
    return data

df = read_text(link)

pd.set_option("display.max_columns",None)


# print(df.dtypes)

# print(df.head(50))

# print(df.info())

df["SKU"] = df["SKU"].astype("string")

df["Product Name"] = df["Product Name"].astype("string")
                 
df["Brand"] = df["Brand"].astype("category")

df['Price'] = pd.to_numeric(df['Price'], errors="coerce")

# df['Price per unit'] = pd.to_numeric(df['Price'], errors="coerce")

df['Ratings'] = pd.to_numeric(df['Ratings'], errors="coerce")

df["Online Only"] = df["Online Only"].astype("category")

df["Package Size"] = df["Package Size"].astype("category")

df['Date'] = pd.to_datetime(df['Date'], errors="coerce")

# print(df.dtypes)

# print(df.isnull().sum())

# df_interpolated = df.interpolate(method="linear")

# print(f"The sum of null values is {df_interpolated.isnull().sum()} after interpolation")

df_deduplicated = df.drop_duplicates() 

# numeric_columns = ["Price", "Ratings"]
# # print(df_interpolated.isnull().sum())

# # constant_columns = df_interpolated.columns[df_interpolated.nunique() == 1]
# # df = df_interpolated.drop(columns = constant_columns)


# Needed to select numerical value after grouping 

# df_brand = df_deduplicated.groupby(["Brand"])["Price"].mean().reset_index()
# df_deduplicated.groupby(["Online Only"])["Price"].mean()
# df_deduplicated.groupby(["Product Name"])["Price"].mean()

# print(f"{df_brand}")


def gen_dates(year_2,month_2,day_2,year_1,month_1,day_1, no_of_dates):
    date_1 = date(year_1,month_1, day_1)
    date_2 = date(year_2,month_2, day_2)

    date_list = [date_1]

    while date_1 != date_2:
        date_1 += timedelta(days = 1)
        date_list.append(date_1)
    return date_list
    

gend_dates = gen_dates(2023,12,31,2021,1,1,len(df))
rand_quantity = randint(1000,100000,len(df))



df = pd.DataFrame(gend_dates,columns=["Updated"])
df = pd.DataFrame(rand_quantity,columns=["Quantity"])

# plt.scatter(df["Qauntity"], df["Price"])

sns.heatmap(df[["Price", "Rating", "Qauntity"]].corr())

print(df.head())

