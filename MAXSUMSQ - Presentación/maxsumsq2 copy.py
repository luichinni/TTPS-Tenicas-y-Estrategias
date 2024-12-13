from sys import stdin, stdout

rta = []

tests = int(stdin.readline())

for _ in range(tests):
    tam_arr = int(stdin.readline())

    num_arr = [int(elem) for elem in stdin.readline().split()]

    maximo = num_arr[0]
    suma_actual = num_arr[0]

    for I in range(1,len(num_arr)):
        # busco la suma maxima de subsecuencia, algoritmo de kadane
        suma_actual = max(suma_actual + num_arr[I], num_arr[I])
        
        maximo = max(suma_actual, maximo)

    # hago suma de prefijos para contar arreglos con cierta propiedad
    acumulado = 0
    acumulados_pasados = {}
    acumulados_pasados[0] = 1 # 0:2 | 2:2 |                                     0:1
    ocurrencias = 0 # 1 -> 2 -> _ -> 4                                          1

    for num in num_arr: # 2 0 -2 2                                              -1 -1 -1
        acumulado += num # 2 -> 2 -> 0 -> 2                                     -1 -> -2
        diferencia = acumulado - maximo # 0 -> 0 -> -2 -> 0                     0 -> -1
        
        if diferencia in acumulados_pasados: # 0 -> 0 -> -2 -> 0                0 -> -1
            ocurrencias += acumulados_pasados[diferencia] # 1 -> 2 -> _ -> 4    1 -> 2

        if acumulado in acumulados_pasados: # 2:1 -> 2:2 -> 0:2                 -1:1 | -2:1
            acumulados_pasados[acumulado] += 1
        else:
            acumulados_pasados[acumulado] = 1
    
    rta.append("{} {}".format(maximo, ocurrencias))

stdout.write("\n".join(rta) + "\n")