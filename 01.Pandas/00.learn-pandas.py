# Cuaderno introductorio para aprender de la libería Pandas

### Parte 1: Introducción ### 

#  Activando el entorno virtual:
#  pip install --upgrade pip
#  pip install pandas

#%% Esto es una celda de ejemplo
print("Introducción a Pandas")
import pandas as pd 
import sys
import numpy as np
print(f"Estamos usando pandas v.{pd.__version__}") 
# %% Series

# Crear una Serie a partir de una lista
data = [1, 2, 3, 4, 5]  # lista
serie = pd.Series(data) # serie

print("lista:")
print(data)
print("")
print("serie:")
print(serie)

#%% Comparación en memoria:

print("lista:", sys.getsizeof(data), "bytes")
print("serie:", sys.getsizeof(serie), "bytes")


# %% Dataframe:


# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

# print("dict:")
print(data)
# print("")
# print("dataframe:") # dataframe == df
# print(df)

#%% Comparación en memoria:

# print("dict:", sys.getsizeof(data), "bytes")
print("df:", sys.getsizeof(df), "bytes")

"""
Para continuar, buscad un dataset, nos vale cualquiera. 
Yo uso este: https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data (1.45Gb)
""" 

# Para ejecutar la siguiente celda se necesita tener el dataset en la misma carpeta

#%% C:/Users/jpons/Code/Ejercicios/Python/01.Pandas/vehicles.csv


# Leer un archivo CSV
df = pd.read_csv('C:/Users/jpons/Code/Ejercicios/Python/01.Pandas/vehicles.csv')

print(df.head())  # Mostrar las primeras 5 filas del DataFrame
#%% Comparación en memoria:

print("df:", sys.getsizeof(df), "bytes")
print(f"Equivale a {sys.getsizeof(df) / 1_000_000_000} Gb")

#%% Accedemos a una columna por nombre -> Serie
region_col = df['region']
print(region_col)
#%% Accedemos a la primera fila -> Serie
"""La primera fila contiene los nombres de columnas del df:"""

primera_fila = df.iloc[0]
print("primera fila:")
print("")
print(primera_fila) # columnas

# El df tiene campo columns:
print(df.columns)   # columnas

segunda_fila = df.iloc[1]
print("segunda fila:")
print("")
print(segunda_fila) # tengo columnas y valores

# Puedo acceder por nombre de col en la fila:
segundo_id = segunda_fila['id']
print("id:", segundo_id)

### Parte 2: Ejemplos de uso de pandas ### 
#%% Acortar el CSV de vehículos


df = pd.read_csv('C:/Users/jpons/Code/Ejercicios/Python/01.Pandas/vehicles.csv') # todas las filas y cols del CSV original -> 1.45Gb

# Crear una copia del DataFrame con las 10 primeras filas
df_copia = df.head(10).copy()

# Guardar en otro CSV:
df_copia.to_csv("C:/Users/jpons/Code/Ejercicios/Python/01.Pandas/vehicles_acortado.csv", index=False) # mechatroner.rainbow-csv CSV Rainbow para visualizar columna por colores
# %% Filtrado de datos en un dataframe


# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

# Filtrar filas donde la edad es mayor de 25
df_filtrado = df[df['Edad'] > 25]

print("df completo:")
print(df)

print("")
print("df filtrado con Edad > 25:")
print(df_filtrado)

print("")
print("Edad == 25")
print(df[df['Edad'] == 25])

print("")
print("20 < Edad < 30")
filtro = (df['Edad'] > 20) & (df['Edad'] < 30) # serie con bool
df_filtrado = df[filtro] # filtra los casos True (filas)
print(df_filtrado)

#%% Agrupaciones


# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Juan'],
    'Edad': [20, 24, 22, 32, 30],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid']
}
df = pd.DataFrame(data)

# Agrupar por la columna 'Ciudad' y calcular la edad promedio:
df_agrupado = df.groupby('Ciudad')['Edad'].mean()

print(df_agrupado)

#%% Manejo de datos en blanco (limpieza de datos)

# Crear un DataFrame con valores faltantes
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, np.nan, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', np.nan, 'Sevilla']
}
df = pd.DataFrame(data)

print("df original:")
print(df)

# Rellenar valores faltantes en la columna 'Edad' con la edad promedio

# df['Edad'].fillna(df['Edad'].mean(), inplace=True) # sintaxis actual -> arroja warning de cambio futuro en 3.0 // vamos por 2.2..

df.fillna({'Edad': df['Edad'].mean()}, inplace=True) # nueva sintaxis para pandas 3.0 // cambio a futuro

print("")
print("df con valores medios en Edad donde había NaN:")
print(df)

# Eliminar filas con valores faltantes
df.dropna(inplace=True)

print("")
print("df sin NaN:")
print(df)