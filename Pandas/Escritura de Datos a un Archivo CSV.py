import pandas as pd

df = pd.read_csv('C:/Users/jpons/Documents/Home/Proveidors/Inkor/Modulo1/python/libs/archivo.csv')
# Suponiendo que df es un DataFrame
df.to_csv('C:/Users/jpons/Documents/Home/Proveidors/Inkor/Modulo1/python/libs/archivo.csv', index=False)