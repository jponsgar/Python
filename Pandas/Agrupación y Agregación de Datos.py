import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Juan', 'Ana', 'Luis', 'Maria', 'Juan'],
    'Edad': [28, 24, 22, 32, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Madrid']
}
df = pd.DataFrame(data)

# Agrupar por la columna 'Ciudad' y calcular la edad promedio
df_agrupado = df.groupby('Ciudad')['Edad'].mean()

print(df_agrupado)

# Ciudad
# Barcelona    24.0
# Madrid       28.0
# Sevilla      32.0
# Valencia     22.0
# Name: Edad, dtype: float64