from urllib.request import urlretrieve
import zipfile
import pandas as pd
import sqlalchemy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Download data
url = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
response = urlretrieve(url, "GTFS.zip")
with zipfile.ZipFile("GTFS.zip") as zip:
    zip.extractall("GTFS")

#Load data with required columns
columns_to_keep = [0,2,4,5,6]  
data = pd.read_csv('GTFS\stops.txt', delimiter=',', usecols = columns_to_keep)
 
data = data[data['zone_id'] == 2001]

#Validate data
data = data[(data.iloc[:, 2] >= -90) & (data.iloc[:, 2] <= 90)]
data = data[(data.iloc[:, 3] >= -90) & (data.iloc[:, 3] <= 90)]

#Save transformed dataframe to sqlite database
data.to_sql('stops', 'sqlite:///gtfs.sqlite', if_exists='replace', index=False)

