#%% Ejemplo de benchmark de algoritmos
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Definir las implementaciones del algoritmo
def sum_for_loop(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def sum_builtin(numbers):
    return sum(numbers)

def sum_numpy(numbers):
    return np.sum(numbers)

# Crear una lista de números para la prueba
numbers = list(range(1_000_000))

# Medir los tiempos de ejecución usando timeit
time_for_loop = timeit.timeit('sum_for_loop(numbers)', globals=globals(), number=100)
time_builtin = timeit.timeit('sum_builtin(numbers)', globals=globals(), number=100)
time_numpy = timeit.timeit('sum_numpy(numbers)', globals=globals(), number=100)

# Imprimir los tiempos de ejecución
print(f'Tiempo usando for loop: {time_for_loop:.6f} segundos')
print(f'Tiempo usando sum builtin: {time_builtin:.6f} segundos')
print(f'Tiempo usando numpy: {time_numpy:.6f} segundos')

# Visualizar los resultados con matplotlib
labels = ['For Loop', 'Sum Builtin', 'Numpy']
times = [time_for_loop, time_builtin, time_numpy]

plt.bar(labels, times, color=['#fdba74', '#fb923c', '#f97316']) # admite colore en HEX
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de ejecución de diversas implementaciones')
plt.show()