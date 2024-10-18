from sys import stdin

tam = []
anterior = []

def LIS(arr: list) -> int:
    # rta en 0
    # por cada nro establecer tam en 1 y anterior en -1
        # por cada anterior
            # si soy menor y mi tam es menor q el +1
                # mi tam es el + 1
                # mi anterior es el
        
        # si el tamñao de rta es menor que el actual
            # rta = actual
    #ret

    rta = 0

    for I in range(len(arr)):

        for J in range(I):
            if (arr[J]<arr[I]) and (tam[I] < tam[J]+1):
                tam[I] = tam[J] + 1
                anterior[I] = J
        
        if (tam[rta] < tam[I]):
            rta = I
    
    return tam[rta]

try:
    while True:
        n = int(input())
        seq = list(map(int,input().split()))

        tam = [1] * n
        anterior = [-1] * n

        print(LIS(seq))
except:
    pass
