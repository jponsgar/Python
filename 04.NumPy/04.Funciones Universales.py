import numpy as np

# Crear un arreglo de ejemplo
arr = np.array([0, np.pi/2, np.pi])

# Aplicar funciones trigonométricas
sin = np.sin(arr)
cos = np.cos(arr)
tan = np.tan(arr)

print(sin)
print(cos)
print(tan)

# [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# [ 1.000000e+00  6.123234e-17 -1.000000e+00]
# [ 0.00000000e+00  1.63312394e+16 -1.22464680e-16]