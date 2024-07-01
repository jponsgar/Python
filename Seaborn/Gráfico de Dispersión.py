import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("iris")

# Crear un gráfico de dispersión
sns.scatterplot(x='sepal_length', y='sepal_width', data=data, hue='species')

# Añadir título y etiquetas
plt.title('Relación entre Sepal Length y Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

# Mostrar el gráfico
plt.show()