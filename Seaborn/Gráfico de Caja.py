import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo
data = sns.load_dataset("tips")

# Crear un gráfico de caja
sns.boxplot(x='day', y='total_bill', data=data)

# Añadir título y etiquetas
plt.title('Distribución de Total Bill por Día')
plt.xlabel('Día')
plt.ylabel('Total Bill')

# Mostrar el gráfico
plt.show()