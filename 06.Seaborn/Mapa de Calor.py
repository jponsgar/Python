import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("iris")

# Calcular la matriz de correlación
correlation_matrix = data.corr()

# Crear un mapa de calor
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Añadir título
plt.title('Matriz de Correlación de Iris')

# Mostrar el gráfico
plt.show()