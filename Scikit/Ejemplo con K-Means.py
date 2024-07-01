
#    Importar Librerías y Dataset

from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#    Cargar el Dataset de Iris

# Cargar el dataset de Iris
iris = datasets.load_iris()
X = iris.data

#    Aplicar K-Means para Agrupar los Datos

# Aplicar K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

#    Visualizar los Clusters

# Visualizar los clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Clusters de Iris con K-Means')
plt.show()