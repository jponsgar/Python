import pandas as pd
import matplotlib.pyplot as plt

# Leer un archivo CSV
df = pd.read_csv('ejercicio_2.csv')

# Crear el DataFrame
data = pd.DataFrame(df)

# Calcular promedios de altura por género
Altura_by_Genero = data.groupby('Genero')['Altura'].mean().reset_index()


# Histograma de alturas
plt.hist(data['Altura'], bins=50, edgecolor='black')
plt.title('Histograma de Alturas')
plt.xlabel('Altura (cm)')
plt.ylabel('Frecuencia')
plt.grid(ls="--", color="#dadada")
plt.show()


# Diagrama de dispersión de pesos vs edades
plt.scatter(data['Edad'], data['Peso'], edgecolor='blue')
plt.title('Diagrama de Dispersión de Pesos vs Edades')
plt.xlabel('Edad (años)')
plt.ylabel('Peso (kg)')
plt.grid(ls="--", color="#dadada")
plt.show()

# Gráfica de barras de promedios de altura por género
plt.bar(Altura_by_Genero['Genero'], Altura_by_Genero['Altura'], color=['blue', 'pink'])
plt.title('Promedio de Alturas por Género')
plt.xlabel('Género')
plt.ylabel('Altura Promedio (cm)')
plt.grid(ls="--", color="#dadada")
plt.show()
