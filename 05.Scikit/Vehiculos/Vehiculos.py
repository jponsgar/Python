import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Leer el fichero vehicles.csv
file_path = 'vehicles.csv'
df = pd.read_csv(file_path)

# Mostrar los primeros registros del dataframe
print(df.head())

# Filtrar las columnas necesarias
df_filtered = df[['year', 'price', 'odometer']].dropna()

# Crear el modelo de regresión lineal para predecir el precio basado en el año y el odómetro
X = df_filtered[['year', 'odometer']]
y = df_filtered['price']

model = LinearRegression()
model.fit(X, y)

# Predicciones
year_range = pd.Series(range(int(df_filtered['year'].min()), int(df_filtered['year'].max()) + 1))
odometer_median = df_filtered['odometer'].median()
pred_data = pd.DataFrame({'year': year_range, 'odometer': odometer_median})
price_pred = model.predict(pred_data)

# Graficar los datos
plt.figure(figsize=(12, 6))

# Gráfico de dispersión de los datos reales
plt.scatter(df_filtered['year'], df_filtered['price'], color='blue', alpha=0.3, label='Datos reales')

# Línea de regresión
plt.plot(year_range, price_pred, color='red', linestyle='--', label='Línea de regresión')

plt.xlabel('Año del vehículo')
plt.ylabel('Precio')
plt.title('Regresión lineal del precio del vehículo basado en el año y el odómetro')
plt.legend()
plt.grid(True)
plt.show()
