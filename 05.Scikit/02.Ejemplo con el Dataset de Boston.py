
#    Importar Librerías y Dataset

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#    Cargar el Dataset de Boston

# Cargar el dataset de Boston
boston = datasets.load_boston()
X = boston.data
y = boston.target

#    Dividir el Dataset en Conjuntos de Entrenamiento y Prueba

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#    Entrenar un Modelo de Regresión Lineal

# Entrenar el modelo de regresión lineal
reg = LinearRegression()
reg.fit(X_train, y_train)

#    Hacer Predicciones y Evaluar el Modelo

# Hacer predicciones
y_pred = reg.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')