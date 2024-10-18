from sys import stdin

def can_distribute(valijas: list, peso: int)->bool:
    columnas = peso + 1
    filas = len(valijas) + 1

    matriz = [[0] * columnas for _ in range(filas)]

    # matriz[item][weights]
    for W in range(1,columnas): # por cada peso
        for V in range(1,filas): # si cuento la valija V
            if (valijas[V-1] <= W): # entra en la valija
                matriz[V][W] = max(matriz[V-1][W],matriz[V-1][W - valijas[V-1]]+valijas[V-1]) # me quedo el maximo peso entre el anterior y el mejor conseguido hasta peso-actual + actual
            else: # si no entra nos quedamos el anterior
                matriz[V][W] = matriz[V-1][W]

    return matriz[filas-1][columnas-1] == peso

entrada = stdin.readlines()

casos = int(entrada[0])

entrada = entrada[1:]

for I in range(casos):
    valijas = list(map(int,entrada[I].split()))

    max_w = sum(valijas)

    if max_w % 2 != 0:
        print("NO")
        continue
    
    half_w = max_w // 2

    es_posible = "YES" if can_distribute(valijas,half_w) else "NO"

    print(es_posible)
