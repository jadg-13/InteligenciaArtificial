from collections import deque

def bfs(grafico, inicio, objetivo):
    cola = deque([(inicio , [inicio])])

    while cola:
        nodo, camino = cola.popleft()

        if nodo == objetivo:
            return camino
        
        for vecino in grafico[nodo]:
            if vecino not in camino:
                cola.append((vecino, camino + [vecino]))

    return None
    
grafo = {
    'A':['B', 'C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F', 'G'],
    'D':['B'],
    'E':['B', 'H'],
    'F':['C'],
    'G':['C'],
    'H':['E']
}

#inicio
inicio = 'A'
#objetivo
objetivo = 'H'

resultado = bfs(grafo, inicio, objetivo)

if resultado:
    print(f"Camino de {inicio} a {objetivo}: {resultado}")
else:
    print(f"NO se encontro el objetivo {objetivo}")