import pandas as pd

airports = pd.read_csv("https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv", sep=";")

airports.to_sql('airports', 'sqlite:///airports.sqlite', if_exists='replace', index=False)