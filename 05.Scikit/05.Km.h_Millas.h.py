import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos: Conversión de km/h a mph (1 km/h ≈ 0.621371 mph)
km_h = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]).reshape(-1, 1)
mph = km_h * 0.621371

# Crear el modelo de regresión lineal
model = LinearRegression()
model.fit(km_h, mph)

# Predicciones
km_h_range = np.linspace(0, 100, 100).reshape(-1, 1)
mph_pred = model.predict(km_h_range)

# Graficar los datos y la línea de regresión
plt.figure(figsize=(10, 6))
plt.scatter(km_h, mph, color='blue', label='Datos reales')
plt.plot(km_h_range, mph_pred, color='red', linestyle='--', label='Línea de regresión')
plt.xlabel('Kilómetros por hora (km/h)')
plt.ylabel('Millas por hora (mph)')
plt.title('Conversión de km/h a mph')
plt.legend()
plt.grid(True)
plt.show()
