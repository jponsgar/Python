import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("tips")

# Crear un histograma y KDE
sns.histplot(data['total_bill'], kde=True)

# Añadir título y etiquetas
plt.title('Distribución de Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frecuencia')

# Mostrar el gráfico
plt.show()