import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Paso 1: Listas de temperaturas en Celsius y Fahrenheit
celsius = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
fahrenheit = np.array([32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212])

# Paso 2: Dividir los datos en conjuntos de entrenamiento y prueba
celsius_train, celsius_test, fahrenheit_train, fahrenheit_test = train_test_split(celsius, fahrenheit, test_size=0.2, random_state=42)

# Paso 3: Entrenar el modelo
model = LinearRegression()
model.fit(celsius_train.reshape(-1, 1), fahrenheit_train)

# Paso 4: Evaluar el modelo
fahrenheit_pred = model.predict(celsius_test.reshape(-1, 1))
mae = mean_absolute_error(fahrenheit_test, fahrenheit_pred)
r2 = r2_score(fahrenheit_test, fahrenheit_pred)

# Verificar que la precisión esté dentro del 5%
percent_error = (mae / np.mean(fahrenheit_test)) * 100
assert percent_error <= 5, "La precisión del modelo no está dentro del 5%"

# Mostrar la ecuación del modelo
coef = model.coef_[0]
intercept = model.intercept_
print(f"Ecuación del modelo: Fahrenheit = {coef:.2f} * Celsius + {intercept:.2f}")

# Paso 5: Visualizar los resultados
plt.scatter(celsius_test, fahrenheit_test, color='blue', label='Valores reales')
plt.plot(celsius_test, fahrenheit_pred, color='red', linestyle='--', label='Predicciones')
plt.xlabel('Temperatura en Celsius')
plt.ylabel('Temperatura en Fahrenheit')
plt.title('Comparación de predicciones vs valores reales')
plt.grid(ls="--", color="#dadada")
plt.show()

# Imprimir métricas de evaluación
print(f"Error absoluto medio (MAE): {mae:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")
print(f"Porcentaje de error: {percent_error:.2f}%")
