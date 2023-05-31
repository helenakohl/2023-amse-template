import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Datasource1: Accident data

accidents = pd.read_csv('https://download.statistik-berlin-brandenburg.de/c2b6d25afa19b607/8d9164595b8b/AfSBBB_BE_LOR_Strasse_Strassenverkehrsunfaelle_2021_Datensatz.csv', sep=';')

# Convert datataypes

accidents["LINREFX"] = [float(str(i).replace(",", ".")) for i in accidents["LINREFX"]]
accidents["LINREFX"] = pd.to_numeric(accidents["LINREFX"])

accidents["LINREFY"] = [float(str(i).replace(",", ".")) for i in accidents["LINREFY"]]
accidents["LINREFY"] = pd.to_numeric(accidents["LINREFY"])

accidents["XGCSWGS84"] = [float(str(i).replace(",", ".")) for i in accidents["XGCSWGS84"]]
accidents["XGCSWGS84"] = pd.to_numeric(accidents["XGCSWGS84"])

accidents["YGCSWGS84"] = [float(str(i).replace(",", ".")) for i in accidents["YGCSWGS84"]]
accidents["YGCSWGS84"] = pd.to_numeric(accidents["YGCSWGS84"])

accidents.to_sql('accidents', 'sqlite:///accidents.sqlite', if_exists='replace', index=False)


# Datasource2: Traffic data

# load information for every traffic sensor
traffic_sensors = pd.read_excel('https://mdhopendata.blob.core.windows.net/verkehrsdetektion/Stammdaten_Verkehrsdetektion_2022_07_20.xlsx')

# traffic data for June (month with highest number of accidents)
traffic_june = pd.read_csv('https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_06.csv.gz', compression='gzip', sep=';')

# add information for traffic sensor
traffic_june = pd.merge(left=traffic_june, right=traffic_sensors, left_on='detid_15', right_on='DET_ID15')

# convert data types
traffic_june['tag'] = pd.to_datetime(traffic_june['tag'], format="%d.%m.%Y")

traffic_june.to_sql('traffic_june', 'sqlite:///traffic_june.sqlite', if_exists='replace', index=False)



# Import data for every month of 2021

#months = {}

#for i in range (1,10):
#    months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_0{i}.csv.gz', compression='gzip', sep=';')
    
#for i in range (10,13):
#   months[i] =  pd.read_csv(f'https://mdhopendata.blob.core.windows.net/verkehrsdetektion/2021/Detektoren%20(einzelne%20Fahrspur)/det_val_hr_2021_{i}.csv.gz', compression='gzip', sep=';')

# Combine all data for 2021
#traffic = pd.concat(months)

# add information for traffic sensor
#traffic = pd.merge(left=traffic, right=traffic_sensors, left_on='detid_15', right_on='DET_ID15')

#traffic.to_sql('traffic', 'sqlite:///traffic.sqlite', if_exists='replace', index=False)