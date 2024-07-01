import pandas as pd

# Una Serie es una estructura de datos unidimensional que puede almacenar cualquier tipo de datos.
# Crear una Serie a partir de una lista
data = [1, 2, 3, 4, 5]
serie = pd.Series(data)

print(serie)

# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64