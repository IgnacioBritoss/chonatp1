import random

# Constantes
N: int = 10  
CANTIDAD_BARCOS: int = 25  
CANTIDAD_DISPAROS: int = 10  

# Tablero vacío
tablero: list[list[bool]] = [[False for _ in range(N)] for _ in range(N)]  

# Función para poner los barcos en posiciones aleatorias
def poner_barcos():
    barcos_puestos: int = 0
    while barcos_puestos < CANTIDAD_BARCOS:
        fila: int = random.randrange(0, N)
        columna: int = random.randrange(0, N)
        
        if tablero[fila][columna] == False:  
            tablero[fila][columna] = True
            barcos_puestos += 1

# Mostrar el tablero final
def mostrar_tablero():
    print("\nTablero final:")
    for fila in tablero:
        print(" ".join("B" if celda else "~" for celda in fila))

# Disparar a una coordenada
def disparar(fila: int, columna: int, aciertos: int, fallos: int):
    if tablero[fila][columna]:  
        print("LE PEGASTE")
        aciertos = aciertos + 1  
        tablero[fila][columna] = False  
    else:
        print("AL AGUA")
        fallos = fallos + 1  
    
    return aciertos, fallos  

# Iniciar el juego
poner_barcos()
print("Debes encontrar " + str(CANTIDAD_BARCOS) + " barcos ocultos en el tablero de " + str(N) + "x" + str(N))

aciertos = 0
fallos = 0

for intento in range(CANTIDAD_DISPAROS):
    print("\nIntento " + str(intento + 1) + " de " + str(CANTIDAD_DISPAROS))
    
    # Pedir coordenadas al usuario
    fila = int(input("Ingresa la fila (0-" + str(N - 1) + "): "))
    columna = int(input("Ingresa la columna (0-" + str(N - 1) + "): "))

    # Validar que las coordenadas estén dentro del rango
    if fila >= 0 and fila < N and columna >= 0 and columna < N:
        aciertos, fallos = disparar(fila, columna, aciertos, fallos)  
    else:
        print("Ingresa valores entre 0 y " + str(N - 1))
        fallos += 1  

# Mostrar resultados finales
print("\nJuego terminado.")
print("Disparos acertados: " + str(aciertos))
print("Disparos fallados: " + str(fallos))
mostrar_tablero()
