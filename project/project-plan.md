# Project Plan

## Summary

<!-- Describe your data science project in max. 5 sentences. -->

This project analyzes traffic accidents in Berlin in 2021. It examines what types of accidents are most common and attempts to identify areas with particularly high accident occurrences. Additionally, a second datasource is used to investigate the effect of different factors in traffic (amount, speed...) on the number and severety of accidents. This way it aims to suggest strategies to prevent traffic accidents. 

## Rationale

<!-- Outline the impact of the analysis, e.g. which pains it solves. -->
Analyzing accident and traffic data has several benefits. 

1. Improving safety: This analysis can help authorities to identify areas with high accident rates and take measures to improve safety, such as installing traffic signals, setting speed limits, and increasing controls in those areas.

2. Infrastructure planning: traffic and accident data can help authorities determine where to invest in infrastructure improvements such as building new roads and bike lanes or expanding public transit services, based on where the most significant traffic or accident problems exist.

3. Enhancing emergency response: Analyzing accident data can help emergency responders understand the most common types of accidents and where they are most likely to occur, allowing them to be better prepared to respond quickly.


## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Statistik der Straßenverkehrsunfälle
* Metadata URL: https://daten.berlin.de/datensaetze/stra%C3%9Fenverkehrsunf%C3%A4lle-nach-unfallort-berlin-2021
* Data URL: https://download.statistik-berlin-brandenburg.de/c2b6d25afa19b607/8d9164595b8b/AfSBBB_BE_LOR_Strasse_Strassenverkehrsunfaelle_2021_Datensatz.csv
* Data Type: CSV

The datasource includes information on accidents that happened in Berlin's traffic during 2021. For each road accident the table contains information on the place (district, street, coordinates), time (month, day, hour) and involved vehicles. Further, the acccidents are classified by their severity and type. 


### Datasource2: Verkehrsdetektion Berlin
* Metadata URL: https://mobilithek.info/offers/-1770265238595584205
* Data URL: https://api.viz.berlin.de/daten/verkehrsdetektion?path=2021%2FDetektoren+%28einzelne+Fahrspur%29%2F
* Data Type: CSV

Each table contains one month of traffic data from Berlin collected by detectors. In addition to the average number of cars and trucks per hour, the average speed was also measured.

An additional table includes information on the detectors, such as their location and exact coordinates:
https://mdhopendata.blob.core.windows.net/verkehrsdetektion/Stammdaten_Verkehrsdetektion_2022_07_20.xlsx


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data pipeline [#1][i1]
2. Data exploration [#2][i2]
3. Data cleaning/prepatation [#3][i3]
4. Reduce dataset [#4][i4]
3. Visualizing data on maps [#5][i5]

[i1]: https://github.com/helenakohl/2023-amse-template/issues/4
[i2]: https://github.com/helenakohl/2023-amse-template/issues/1
[i3]: https://github.com/helenakohl/2023-amse-template/issues/2
[i4]: https://github.com/helenakohl/2023-amse-template/issues/5
[i5]: https://github.com/helenakohl/2023-amse-template/issues/3
