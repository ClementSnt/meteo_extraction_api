!pip install meteostat
import pandas as pd
from meteostat import Point, Daily
from datetime import datetime

# sélection de la plage de dates souhaitées 
start_date = datetime(2025, 9, 30)
end_date = datetime(2025, 10, 20)

# Sélection du lieu géographique, ici Paris par exemple
location = Point(48.8666, 2.3333)

# Récupération des données
data = Daily(location, start_date, end_date)
data = data.fetch()

# Sélection des colonnes utiles pour le cas (notamment possible de rajouter neige, force du vent, direction du vent, ensoleillement)
df = data[['tavg','tmax','tmin','prcp']]
df = df.reset_index()

# ajout du mois et de l'année pour filtrer si besoin etc
df['month'] = df['time'].dt.month
df['year'] = df['time'].dt.year

# export en csv
df.to_csv('meteo_paris.csv')
print('export fait')
