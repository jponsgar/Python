import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria'],
    'Edad': [28, 24, 22, 32],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}
df = pd.DataFrame(data)

# Filtrar filas donde la edad es mayor de 25
df_filtrado = df[df['Edad'] > 25]

print(df_filtrado)

#   Nombre  Edad   Ciudad
# 0   Juan    28   Madrid
# 3  Maria    32  Sevilla