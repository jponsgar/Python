import pandas as pd

# Un DataFrame es una estructura de datos bidimensional con columnas de potencialmente diferentes tipos.
# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

print(df)

#   Nombre  Edad     Ciudad
# 0   Juan    28     Madrid
# 1    Ana    24  Barcelona
# 2   Luis    22   Valencia
# 3  Maria    32    Sevilla