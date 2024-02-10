import math

def minimax(tablero, profundidad, es_maximizando):
    if ganador(tablero, 'X'):
        return -1
    elif ganador(tablero, 'O'):
        return 1
    elif tablero_lleno(tablero):
        return 0

    if es_maximizando:
        mejor_valor = -math.inf
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = 'O'
                    valor = minimax(tablero, profundidad + 1, False)
                    tablero[fila][columna] = ''
                    mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = math.inf
        for fila in range(3):
            for columna in range(3):
                if tablero[fila][columna] == '':
                    tablero[fila][columna] = 'X'
                    valor = minimax(tablero, profundidad + 1, True)
                    tablero[fila][columna] = ''
                    mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def movimiento_optimo(tablero):
    mejor_valor = -math.inf
    mejor_movimiento = (-1, -1)

    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == '':
                tablero[fila][columna] = 'O'
                valor = minimax(tablero, 0, False)
                tablero[fila][columna] = ''

                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = (fila, columna)

    return mejor_movimiento

def ganador(tablero, jugador):
    # Verifica filas y columnas
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True

    # Verifica diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    return all(all(cell != '' for cell in row) for row in tablero)

def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)


# Ejemplo de uso
tablero_inicial = [['', '', ''], ['', '', ''], ['', '', '']]
turno = 'X'

while not ganador(tablero_inicial, 'X') and not ganador(tablero_inicial, 'O') and not tablero_lleno(tablero_inicial):
    imprimir_tablero(tablero_inicial)

    if turno == 'X':
        fila, columna = map(int, input("Ingrese su movimiento (fila y columna separados por espacio): ").split())
        if tablero_inicial[fila][columna] == '':
            tablero_inicial[fila][columna] = 'X'
            turno = 'O'
    else:
        fila, columna = movimiento_optimo(tablero_inicial)
        tablero_inicial[fila][columna] = 'O'
        turno = 'X'

imprimir_tablero(tablero_inicial)

if ganador(tablero_inicial, 'X'):
    print("¡Ganaste!")
elif ganador(tablero_inicial, 'O'):
    print("¡La computadora ganó!")
else:
    print("Empate.")
