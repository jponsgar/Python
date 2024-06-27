# Si Los ids para cada variable son distintos:
# Esto implica que se guardan en posiciones de memoria distintos
# -------------------------------------------------------------------------------------
# Asignación a un mismo valor
x = y = z = "algo"
print(x, y, z)  # algo algo algo
# -------------------------------------------------------------------------------------
# Aparecen x, y, z con el mismo id:
print("x en:", id(x))
print("y en:", id(y))
print("z en:", id(z))
# -------------------------------------------------------------------------------------
x = "patata"
print(x, y, z) # patata algo algo
# -------------------------------------------------------------------------------------
print("x en:", id(x))  # cambia posición memoria
print("y en:", id(y))
print("z en:", id(z))
# -------------------------------------------------------------------------------------
# EJEMPLOS
# Lista y desempaquetar en variables:
datos = ["1", "2", "3"]
a, b, c = datos
print(a, b, c)  # 1 2 3
# -------------------------------------------------------------------------------------
# Con un elemento de menos, no cuela:
datos = ["1", "2", "3"]
a, b = datos # Error hay 2 elementos a la izq y 3 a la derecha
print(a, b, c) # 1 2 3
# -------------------------------------------------------------------------------------
# Con un elemento de más, no cuela:
datos = ["1", "2", "3"]
a, b, c, d = datos # Error hay 4 elementos a la izq y 3 a la derecha
print(a, b, c) # 1 2 3
# -------------------------------------------------------------------------------------
# Si solo queremos dos elementos:
datos = ["1", "2", "3"]
a, b, _ = datos # _ es un comodín, hay que definir los tres
print(a, b)  # 1 2