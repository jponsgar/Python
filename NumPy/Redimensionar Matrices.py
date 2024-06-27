import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Redimensionar a 3x2
reshaped = arr.reshape((3, 2))
print(reshaped)

# [[1 2]
#  [3 4]
#  [5 6]]