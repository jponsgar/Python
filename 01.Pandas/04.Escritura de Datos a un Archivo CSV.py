import pandas as pd

df = pd.read_csv('C:/Users/jpons/Code/Ejercicios/Python/Pandas/archivo.csv')
# Suponiendo que df es un DataFrame
df.to_csv('C:/Users/jpons/Code/Ejercicios/Python/Pandas/archivo.csv', index=False)