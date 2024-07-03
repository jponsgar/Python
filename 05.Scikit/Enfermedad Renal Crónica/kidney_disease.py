import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Cargar los datos
data = pd.read_csv('kidney_disease.csv')

# Preprocesar los datos (eliminar filas con valores faltantes)
data = data.dropna()

# Convertir la variable categórica 'hipertension' a numérica
data['hipertension'] = data['hipertension'].apply(lambda x: 1 if x == 'yes' else 0)

# Separar las características y la variable objetivo
X = data[['edad', 'presion_arterial', 'albumina', 'glucosa', 'urea_sangre', 
          'creatinina_serica', 'sodio', 'potasio', 'hemoglobina', 
          'recuento_globulos_blancos', 'recuento_globulos_rojos', 'hipertension']]
y = data['clasificacion']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Calcular la precisión (asumimos precisión como el porcentaje de varianza explicada)
precision = r2 * 100

# Mostrar la ecuación del modelo
print("Ecuación del modelo:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")
print(f"Intercepto: {model.intercept_:.4f}")

# Mostrar métricas de evaluación
print(f"\nMean Squared Error: {mse:.4f}")
print(f"R-squared: {r2:.4f}")
print(f"Precisión: {precision:.2f}%")

# Visualizar los resultados de las predicciones vs los valores reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=2)
plt.xlabel('Valores Reales')
plt.ylabel('Predicciones')
plt.title('Predicciones vs Valores Reales')
plt.show()

