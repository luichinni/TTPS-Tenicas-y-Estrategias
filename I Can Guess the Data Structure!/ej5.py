from sys import stdin
from collections import deque

entrada = [[int(num) for num in linea.split()] for linea in stdin]

linea_actual = 0

while (linea_actual < len(entrada)):
    casos = entrada[linea_actual][0]
    linea_actual+=1

    valida = [True] * 3

    cola = deque()
    pila = []
    cola_p = []

    linea_ant = linea_actual-1
    while (linea_actual < linea_ant+casos and any(valida)):
        if (entrada[linea_actual][0] == 1):
            cola.append(entrada[linea_actual][1])
            pila.append(entrada[linea_actual][1])
            cola_p.append(entrada[linea_actual][1])
        else:
            if not entrada[linea_actual][1] in cola or entrada[linea_actual][1] in pila or entrada[linea_actual][1] in cola_p:
                valida = [False] * 3
            else:
                if valida[0]:
                    if cola.popleft() != entrada[linea_actual][1]:
                        valida[0] = False
                if valida[1]:
                    if pila.pop() != entrada[linea_actual][1]:
                        valida[1] = False
                if valida[2]:
                    if max(cola_p) != entrada[linea_actual][1]:
                        valida[2] = False
                    else:
                        cola_p.remove(max(cola_p))
        
        linea_actual+=1
    
    linea_actual += casos - 1
    
    if (valida.count(True) == 0):
        print('impossible')
    elif (valida.count(True) > 1):
        print('not sure')
    else:
        if valida[0]:
            print('queue')
        elif valida[1]:
            print('stack')
        else:
            print('priority queue')