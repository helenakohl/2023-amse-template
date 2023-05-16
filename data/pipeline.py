import pandas as pd

# Datasource1: Accident data

accidents = pd.read_csv('https://download.statistik-berlin-brandenburg.de/c2b6d25afa19b607/8d9164595b8b/AfSBBB_BE_LOR_Strasse_Strassenverkehrsunfaelle_2021_Datensatz.csv', sep=';')

accidents.to_sql('accidents', 'sqlite:///accidents.sqlite', if_exists='replace', index=False)


# Datasource2: Traffic data

# Import data for every month of 2021

months = {}

for i in range (1,10):
    months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_0{i}.csv.gz', compression='gzip', sep=';')
    
for i in range (10,13):
    months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_{i}.csv.gz', compression='gzip', sep=';')

# Combine all data for 2021

traffic = pd.concat(months)

# Load and add information for every traffic sensor

traffic_sensors = pd.read_excel('https://mdhopendata.blob.core.windows.net/verkehrsdetektion/Stammdaten_Verkehrsdetektion_2022_07_20.xlsx')

traffic = pd.merge(left=traffic, right=traffic_sensors, left_on='detid_15', right_on='DET_ID15')

traffic.to_sql('traffic', 'sqlite:///traffic.sqlite', if_exists='replace', index=False)