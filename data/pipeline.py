import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Datasource1: Accident data
accidents = pd.read_csv('https://download.statistik-berlin-brandenburg.de/c2b6d25afa19b607/8d9164595b8b/AfSBBB_BE_LOR_Strasse_Strassenverkehrsunfaelle_2021_Datensatz.csv', sep=';')

# drop irrlevant columns
irrelevant = ['LINREFX', 'LINREFY']
accidents = accidents.drop(columns=irrelevant)

# Convert datataypes
accidents["XGCSWGS84"] = [float(str(i).replace(",", ".")) for i in accidents["XGCSWGS84"]]
accidents["XGCSWGS84"] = pd.to_numeric(accidents["XGCSWGS84"])

accidents["YGCSWGS84"] = [float(str(i).replace(",", ".")) for i in accidents["YGCSWGS84"]]
accidents["YGCSWGS84"] = pd.to_numeric(accidents["YGCSWGS84"])

accidents.to_sql('accidents', 'sqlite:///accidents.sqlite', if_exists='replace', index=False)


# Datasource2: Traffic data
# This dataset is very big and therefore needs to be reduced for the anaysis, this is done in two ways: 

# 1. data is available in seperate files for each month and we can reduce the time frame to one month

# define month to download
month = '06'

# traffic data for June (month with highest number of accidents)
traffic_month = pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_{month}.csv.gz', compression='gzip', sep=';')

# convert data types
traffic_month['tag'] = pd.to_datetime(traffic_month['tag'], format="%d.%m.%Y")

# load information for every traffic sensor
traffic_sensors = pd.read_excel('https://mdhopendata.blob.core.windows.net/verkehrsdetektion/Stammdaten_Verkehrsdetektion_2022_07_20.xlsx')

# add information for traffic sensor
traffic_month = pd.merge(left=traffic_month, right=traffic_sensors, left_on='detid_15', right_on='DET_ID15')

# drop irrlevant columns
irrelevant2 = ['ABBAUDATUM', 'DEINSTALLIERT', 'KOMMENTAR']
traffic_month = traffic_month.drop(columns=irrelevant2)


traffic_month.to_sql('traffic_month', 'sqlite:///traffic.sqlite', if_exists='replace', index=False)



# 2. Inlcude all months of 21 and combine them, but aggregate the hourly data to daily averages and drop some columns

months = {}

for i in range (1,10):
    months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_0{i}.csv.gz', compression='gzip', sep=';')
    months[i] = months[i].groupby(["detid_15","tag"], as_index=False)[["qualitaet","q_kfz_det_hr","v_kfz_det_hr","q_pkw_det_hr","v_pkw_det_hr","q_lkw_det_hr","v_lkw_det_hr"]].mean()

for i in range (10,13):
    months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_{i}.csv.gz', compression='gzip', sep=';')
    months[i] = months[i].groupby(["detid_15","tag"], as_index=False)[["qualitaet","q_kfz_det_hr","v_kfz_det_hr","q_pkw_det_hr","v_pkw_det_hr","q_lkw_det_hr","v_lkw_det_hr"]].mean()

# Combine all data for 2021
traffic_2021 = pd.concat(months)

# add information for traffic sensor
traffic_2021 = pd.merge(left=traffic_2021, right=traffic_sensors, left_on='detid_15', right_on='DET_ID15')


# drop irrlevant columns
traffic_2021 = traffic_2021.drop(columns=irrelevant2)

traffic_2021.to_sql('traffic_2021', 'sqlite:///traffic.sqlite', if_exists='replace', index=False)