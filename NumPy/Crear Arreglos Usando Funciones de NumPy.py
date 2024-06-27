import numpy as np

# Crear un arreglo de ceros
zeros = np.zeros((3, 4))
print(zeros)

# Crear un arreglo de unos
ones = np.ones((2, 3))
print(ones)

# Crear un arreglo con valores aleatorios
random = np.random.random((2, 2))
print(random)

# Crear un arreglo con valores espaciados uniformemente
linspace = np.linspace(0, 10, 5)
print(linspace)

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
# [[1. 1. 1.]
#  [1. 1. 1.]]
# [[0.08715254 0.13370581]
#  [0.46248944 0.67307562]]
# [ 0.   2.5  5.   7.5 10. ]