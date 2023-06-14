import pandas as pd

columns_to_keep = [0,1,2,12,22,32,42,52,62,72]
df = pd.read_csv('https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv', sep = ';', encoding='latin-1', dtype = {1: str}, skiprows = 6, usecols = columns_to_keep)

df = df[:-4]

column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
df.columns = column_names

df = df[df['CIN'].str.len() != 5]

postive_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

for column in postive_columns:
    df = df[df[column] > 0]

df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
