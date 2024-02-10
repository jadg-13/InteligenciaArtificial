import heapq

def a_estrella(grafico, inicio, objetivo, heuristica):
    cola_prioridad = [(0, inicio, [])]
    visitados = set()

    while cola_prioridad:
        costo_actual, nodo_actual, camino_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            return camino_actual + [nodo_actual]

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo in grafico[nodo_actual].items():
                nuevo_costo = costo_actual + costo
                heuristico = heuristica(vecino, objetivo)
                heapq.heappush(cola_prioridad, (nuevo_costo + heuristico, vecino, camino_actual + [nodo_actual]))

    return None


# Función heurística simple basada en la longitud de las cadenas
def heuristica_simple(nodo_actual, objetivo):
    return abs(len(nodo_actual) - len(objetivo))

# Ejemplo de un grafo ponderado representado como un diccionario de diccionarios
# Los valores son diccionarios donde las claves son nodos vecinos y los valores son costos
grafo_ponderado = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1},
    'E': {'C': 3},
}


inicio = 'A'
objetivo = 'B'

resultado = a_estrella(grafo_ponderado, inicio, objetivo, heuristica_simple)

if resultado:
    print(f"Camino de {inicio} a {objetivo}: {resultado}")
else:
    print(f"No se encontró un camino de {inicio} a {objetivo}")