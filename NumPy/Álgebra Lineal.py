import numpy as np

# Crear una matriz de ejemplo
matrix = np.array([[1, 2], [3, 4]])

# Calcular el determinante
det = np.linalg.det(matrix)
print(det)

# Calcular la inversa
inverse = np.linalg.inv(matrix)
print(inverse)

# -2.0000000000000004
# [[-2.   1. ]
#  [ 1.5 -0.5]]