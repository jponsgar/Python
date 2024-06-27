import pandas as pd
import numpy as np

# Crear un DataFrame con valores faltantes
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, np.nan, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', np.nan, 'Sevilla']
}
df = pd.DataFrame(data)

# Rellenar valores faltantes en la columna 'Edad' con la edad promedio
df['Edad'].fillna(df['Edad'].mean(), inplace=True)

# Eliminar filas con valores faltantes
df.dropna(inplace=True)

print(df)

#   df['Edad'].fillna(df['Edad'].mean(), inplace=True)
#   Nombre       Edad     Ciudad
# 0   Juan  28.000000     Madrid
# 1    Ana  27.333333  Barcelona
# 3  Maria  32.000000    Sevilla