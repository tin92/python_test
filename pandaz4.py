import pandas as pd
import requests
import datetime
from io import StringIO

link = "http://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

def read_text(web: str):
    respons = requests.get(web)
    data = pd.read_csv(StringIO(respons.text))
    return data

df = read_text(link)

pd.set_option("display.max_columns",None)

print(df.dtypes)

# print(df.head(50))

# print(df.info())

df["SKU"] = df["SKU"].astype("string")

df['Price'] = pd.to_numeric(df['Price'], errors="coerce")

df['Price per unit'] = pd.to_numeric(df['Price'], errors="coerce")

df['Ratings'] = pd.to_numeric(df['Ratings'], errors="coerce")

df["Online Only"] = df["Online Only"].astype("category")

df['Date'] = pd.to_datetime(df['Date'], errors="coerce")

print(df.dtypes)

print(f"The sum of null values is {df.isnull().sum()} before interpolation")

df_interpolated = df.interpolate(method="polynomial", order = 3)

print(f"The sum of null values is {df_interpolated.isnull().sum()} after interpolation")

df_deduplicated = df_interpolated.drop_duplicates() 


# print(df_interpolated.isnull().sum())

# constant_columns = df_interpolated.columns[df_interpolated.nunique() == 1]
# df = df_interpolated.drop(columns = constant_columns)

df_deduplicated.groupby(["Brand"]).mean()
df_deduplicated.groupby(["Online Only"]).mean()
df_deduplicated.groupby(["Product Name"]).sum()