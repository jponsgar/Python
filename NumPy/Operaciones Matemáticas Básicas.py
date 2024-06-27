import numpy as np

# Crear arreglos de ejemplo
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Suma de arreglos
suma = a + b
print(suma)

# Resta de arreglos
resta = a - b
print(resta)

# Producto elemento a elemento
producto = a * b
print(producto)

# División elemento a elemento
division = a / b
print(division)

# Producto punto
producto_punto = np.dot(a, b)
print(producto_punto)

# [ 6  8 10 12]
# [-4 -4 -4 -4]
# [ 5 12 21 32]
# [0.2        0.33333333 0.42857143 0.5       ]
# 70