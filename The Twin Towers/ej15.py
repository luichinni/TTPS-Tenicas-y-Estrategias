from sys import stdin

def LCS(torre1: list, torre2: list) -> int:
    """
              t1  
        | - |+1 | a | b |
    t   |+1 | 0 | 0 | 0 |
    2   | a | 0 | 1 | 1 |
        | b | 0 | 1 | 2 |
    
    """

    columnas = len(torre1)+1 # X
    filas = len(torre2)+1 # Y

    matriz = [[0] * columnas for _ in range(filas)]

    for Y in range(1,filas):
        for X in range(1,columnas):
            if (torre1[X-1] == torre2[Y-1]):
                matriz[Y][X] = matriz[Y-1][X-1] + 1
            else:
                matriz[Y][X] = max(matriz[Y-1][X],matriz[Y][X-1])
        
    return matriz[-1][-1]


pares_procesados = 0

while stdin:
    t1, t2 = stdin.readline().split()
    if t1 == '0' and t2 == '0':
        break

    torre1 = list(map(int,stdin.readline().split()))

    torre2 = list(map(int,stdin.readline().split()))

    tiles = LCS(torre1,torre2)

    pares_procesados += 1

    print(f"Twin Towers #{pares_procesados}\nNumber of Tiles : {tiles}\n")

