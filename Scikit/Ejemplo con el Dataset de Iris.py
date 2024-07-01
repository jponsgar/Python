
#   Importar Librerías y Dataset

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#    Cargar el Dataset de Iris

# Cargar el dataset de Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

#    Dividir el Dataset en Conjuntos de Entrenamiento y Prueba

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#    Estandarizar los Datos

# Estandarizar las características
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#    Entrenar un Modelo de Clasificación (K-Nearest Neighbors)

# Entrenar el modelo K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

#    Hacer Predicciones y Evaluar el Modelo

# Hacer predicciones
y_pred = knn.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
