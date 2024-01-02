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

# print(df.head())

# print(df.info())

df["SKU"] = df["SKU"].astype("string")

df['Price'] = pd.to_numeric(df['Price'], errors="coerce")

df['Price per unit'] = pd.to_numeric(df['Price'], errors="coerce")

df['Ratings'] = pd.to_numeric(df['Ratings'], errors="coerce")

df["Online Only"] = df["Online Only"].astype("category")

pd.to_datetime(df['Date'], errors="coerce",inplace=True)

df_interpolated = df.interpolate(method="polynomial", limit_direction="backward")

df_deduplicated = df_interpolated.drop_duplicates() 

# print(df_interpolated.head())

# print(df.info())

print(df.isnull().sum())

print(df_interpolated.isnull().sum())


                
