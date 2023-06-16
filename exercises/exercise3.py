import pandas as pd


# load data with required columns and irgnore the first 6 rows
columns_to_keep = [0,1,2,12,22,32,42,52,62,72]
df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv', sep = ';', encoding='latin-1', dtype = {1: str}, skiprows = 6, usecols = columns_to_keep)

# drop the last 4 rows
df = df[:-4]

# rename the columns
column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
df.columns = column_names

# remove columns with invalid CIN values
df = df[df['CIN'].str.len() == 5]

# remove rows with non-positive values in the other columns
postive_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

for column in postive_columns:
    df = df[df[column] != '-']

df[postive_columns] = df[postive_columns].astype(int)

for column in postive_columns:
    df = df[df[column] > 0]

# save transformed dataframe to sqlite database
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
