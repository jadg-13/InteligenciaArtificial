# Universidad del Valle - Inteligencia Artificial
# Tema: Aprendizaje inductivo 
# Autor: JADG13
# Importar las bibliotecas necesarias
from sklearn.linear_model import LinearRegression
from os import system as system

# Datos de entrenamiento: Kilobytes (Kb)
X_train = [[1024], [2048], [3072], [4096], [5120], [6144], [7168], [8192]]

# Etiquetas: Megabytes (MB)
y_train = [1, 2, 3, 4, 5, 6, 7, 8]

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Limpiar la consola
system("cls")
#pedir el valor de kb
kb = int(input("Ingrese el valor en Kb: "))

# Realizar predicciones
kb_to_convert = [[kb]]
predicted_mb = model.predict(kb_to_convert)

# Imprimir resultado
print(f"{kb} Kb equivalen aproximadamente a {predicted_mb[0]} MB")
