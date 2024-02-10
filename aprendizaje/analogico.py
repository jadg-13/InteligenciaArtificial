# Universidad Del Valle - Inteligencia Artificial
# Tema: Aprendizaje analógico
# Autor: JADG13
# Importar las bibliotecas necesarias
from sklearn.neighbors import NearestNeighbors
import numpy as np

# Datos conocidos (entrenamiento)
X_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])

# Datos desconocidos (nuevas observaciones)
X_unknown = np.array([[1.5, 2.5], [3.5, 4.5]])

# Crear y ajustar el modelo de vecinos más cercanos (Nearest Neighbors)
model = NearestNeighbors(n_neighbors=2)
model.fit(X_train)

# Encontrar los vecinos más cercanos para las nuevas observaciones
distances, indices = model.kneighbors(X_unknown)

# Imprimir los vecinos más cercanos encontrados
for i in range(len(X_unknown)):
    print("Para la observación", X_unknown[i], "los vecinos más cercanos son:", X_train[indices[i]])
