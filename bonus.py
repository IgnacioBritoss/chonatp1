# Constantes
N: int = 5
CANTIDAD_BARCOS: int = 3
CANTIDAD_DISPAROS: int = 5

# Tableros
tablero_j1: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]
tablero_j2: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]

# Función para que un jugador ponga los barcos
def poner_barcos(jugador: int, tablero: list[list[bool]]):
    print("\nJugador " + str(jugador) + ", pone tus " + str(CANTIDAD_BARCOS) + " barcos.")
    barcos_puestos: int = 0
    while barcos_puestos < CANTIDAD_BARCOS:
        fila: int = int(input("Fila del barco " + str(barcos_puestos + 1) + ": "))
        columna: int = int(input("Columna del barco " + str(barcos_puestos + 1) + ": "))
        
        if fila >= 0 and fila < N and columna >= 0 and columna < N:
            if tablero[fila][columna] == False:
                tablero[fila][columna] = True
                barcos_puestos += 1
            else:
                print("Ya hay un barco en esa posicion.")
        else:
            print("Coordenadas fuera de rango.")

# Función para mostrar un tablero 
def mostrar_tablero(tablero: list[list[bool]]):
    for fila in tablero:
        print(" ".join("B" if celda else "~" for celda in fila))

# Función para disparar
def disparar(fila: int, columna: int, tablero: list[list[bool]], aciertos: int):
    if tablero[fila][columna]:
        print("LE PEGASTE")
        aciertos = aciertos + 1
        tablero[fila][columna] = False
    else:
        print("AL AGUA")
    return aciertos

# Poner barcos
poner_barcos(1, tablero_j1)
poner_barcos(2, tablero_j2)

aciertos_j1 = 0
aciertos_j2 = 0

# Disparo
for intento in range(CANTIDAD_DISPAROS):
    print("\nTurno del Jugador 1")
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if fila >= 0 and fila < N and columna >= 0 and columna < N:
        aciertos_j1 = disparar(fila, columna, tablero_j2, aciertos_j1)
    else:
        print("Coordenadas invalidas.")

    print("\nTurno del Jugador 2")
    fila = int(input("Fila: "))
    columna = int(input("Columna: "))
    if fila >= 0 and fila < N and columna >= 0 and columna < N:
        aciertos_j2 = disparar(fila, columna, tablero_j1, aciertos_j2)
    else:
        print("Coordenadas invalidas.")

# Resultados
print("\nFin.")
print("Jugador 1 acerto: " + str(aciertos_j1))
print("Jugador 2 acerto: " + str(aciertos_j2))

if aciertos_j1 > aciertos_j2:
    print("Gano el jugador 1")
elif aciertos_j2 > aciertos_j1:
    print("Gano el jugador 2")
else:
    print("Empate")

# Tableros finales ALTO EXTRA
print("\nTablero final del Jugador 1:")
mostrar_tablero(tablero_j1)
print("\nTablero final del Jugador 2:")
mostrar_tablero(tablero_j2)
