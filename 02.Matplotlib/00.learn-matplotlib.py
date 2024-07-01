# Introducción a matplotlib

"""Activando el entorno virtual
  pip install matplotlib
"""
#%% print de la versión
import matplotlib
print(f"Estamos usando matplotlib v.{matplotlib.__version__}")
import matplotlib.pyplot as plt # importación estándar

#%% Gráfico de línea
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de líneas
plt.plot(x, y)

# Añadir título y etiquetas
plt.title('Gráfico de Líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar el gráfico
plt.show()

#%% Gráfico de barras
import matplotlib.pyplot as plt

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores = [5, 7, 3, 8]

# Crear el gráfico de barras
plt.bar(categorias, valores)

# Añadir título y etiquetas
plt.title('Gráfico de Barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')

# Mostrar el gráfico
plt.show()

#%% Histograma
import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [1, 2, 2, 3, 3, 4, 4, 4, 4, 5]

# Crear el histograma
plt.hist(datos, bins=5, edgecolor='black') # edgecolor también recibe HEX

# Añadir título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()

#%% Scatter o dispersión
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Añadir título y etiquetas
plt.title('Gráfico de Dispersión')
plt.xlabel('X')
plt.ylabel('Y')

# Mostrar el gráfico
plt.show()

#%% Sectores
import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['Python', 'Javascript', 'C#', 'Java', 'Otros']
tamanos = [33, 30, 17, 10, 10]

# Crear el gráfico de sectores
plt.pie(tamanos, labels=etiquetas, autopct='%1.0f%%', startangle=90)

# Añadir título
plt.title('Lenguajes de Programación más usados')

# Asegurar que el gráfico sea circular
plt.axis('equal')

# Mostrar el gráfico
plt.show()
# %% 3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Datos de ejemplo
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Crear la figura y el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear el gráfico de superficie
ax.plot_surface(x, y, z, cmap='inferno') # cmap son códigos de color para añadir a la gráfica https://matplotlib.org/stable/users/explain/colors/colormaps.html

# Añadir título y etiquetas
ax.set_title('Gráfico 3D')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar el gráfico
plt.show()
