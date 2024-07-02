import numpy as np
import time
import sys

# Lista y un Array numpy con un millón de elementos
python_list = list(range(1,1000000))
numpy_array = np.arange(start=1, stop=1000000, step=1)

# Tiempo y Memoria suma - Lista
start_time = time.time()
sum_list = sum(python_list)
list_sum_time = time.time() - start_time
print("Tiempo de suma (Lista Python):", list_sum_time, "segundos")
print("Memoria de suma (Lista Python):", sys.getsizeof(sum_list), "bytes")
print()

# Tiempo y Memoria suma - Array
start_time = time.time()
sum_array = np.sum(numpy_array)
array_sum_time = time.time() - start_time
print("Tiempo de suma (Array NumPy):", array_sum_time, "segundos")
print("Memoria de suma (Array NumPy):", sys.getsizeof(sum_array), "bytes")
print()

# Tiempo y Memoria multiplicación - Lista 
start_time = time.time()
mul_list = [x * 2 for x in python_list]
list_mul_time = time.time() - start_time
print("Tiempo de multiplicación (Lista Python):", list_mul_time, "segundos")
print("Memoria de multiplicación (Lista Python):", sys.getsizeof(mul_list), "bytes")
print()

# Tiempo y Memoria multiplicación - Array 
start_time = time.time()
mul_array = numpy_array * 2
array_mul_time = time.time() - start_time
print("Tiempo de multiplicación (Array NumPy):", array_mul_time, "segundos")
print("Memoria de multiplicación (Array NumPy):", sys.getsizeof(mul_array), "bytes")
