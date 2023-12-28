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

# print(df.head(5))

# Check data types of the columns 

# print(df.dtypes)

print(df["Price"].head(5))
print(df["New Product"].head(5))
print(df["Date"].head(5))
print(df["Online Only"].head(5))
print(df["Availability"].head(5))

print(df["New Product"].unique())
print(df["Date"].unique())
print(df["Online Only"].unique())
print(df["Availability"].unique())

# Convert each column to relevant data type 

df["Price"].astype(float)

#  Tobacco product? 
# df["Availability"].astype(bool)

df["Date"].astype(datetime)

df["Ratings"].astype(float)

# final check 

print(df.dtypes)
