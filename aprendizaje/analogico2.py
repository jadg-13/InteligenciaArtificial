from sklearn.neighbors import NearestNeighbors
import numpy as np

# Datos de películas y preferencias de usuario conocidas (entrenamiento)
# Cada fila representa una película y las columnas representan diferentes características o géneros de películas
# En este ejemplo, se utilizan tres características ficticias para simplificar: Acción, Comedia y Drama
movies_data = np.array([[1, 0, 1],  # Película 1: Acción, Drama
                        [0, 1, 1],  # Película 2: Comedia, Drama
                        [1, 1, 0],  # Película 3: Acción, Comedia
                        [1, 1, 1 ],  # Película 4: Acción, Comedia, Drama
                        [1, 0, 0],  # Película 3: Acción
                        [0, 1, 0],  # Película 4: Comedia
                        [0, 0, 1]]) # Película 5: Drama

# Supongamos que un usuario tiene las siguientes preferencias: Acción = 1, Comedia = 0, Drama = 1
user_preferences = np.array([[1, 0, 1]])

# Crear y ajustar el modelo de vecinos más cercanos (Nearest Neighbors) basado en las preferencias de usuario
model = NearestNeighbors(n_neighbors=2)
model.fit(movies_data)

# Encontrar las películas más similares a las preferencias del usuario
distances, indices = model.kneighbors(user_preferences)

# Imprimir las películas recomendadas
print("Las películas recomendadas para el usuario son:")
for i in range(len(indices[0])):
    print("Película", indices[0][i] + 1)  # Se suma 1 porque los índices se basan en 0 en Python
