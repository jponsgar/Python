import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("flights")

# Crear un gráfico de líneas
sns.lineplot(x='year', y='passengers', data=data)

# Añadir título y etiquetas
plt.title('Pasajeros a lo Largo del Tiempo')
plt.xlabel('Año')
plt.ylabel('Pasajeros')

# Mostrar el gráfico
plt.show()