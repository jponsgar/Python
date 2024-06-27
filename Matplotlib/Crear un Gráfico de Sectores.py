import matplotlib.pyplot as plt

# Datos de ejemplo
etiquetas = ['A', 'B', 'C', 'D']
tamanos = [15, 30, 45, 10]

# Crear el gráfico de sectores
plt.pie(tamanos, labels=etiquetas, autopct='%1.1f%%', startangle=90)

# Añadir título
plt.title('Gráfico de Sectores')

# Asegurar que el gráfico sea circular
plt.axis('equal')

# Mostrar el gráfico
plt.show()

# gráfico de sectores.PNG