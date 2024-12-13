from sys import stdin, stdout

rta = []

tests = int(stdin.readline())

for _ in range(tests):
    tam_arr = int(stdin.readline())

    num_arr = [int(elem) for elem in stdin.readline().split()]

    maximo = num_arr[0]
    suma_actual = num_arr[0]

    for I in range(1,tam_arr):
        # continuamos la busqueda con el acumulado que sea mayor
        suma_actual = max(suma_actual + num_arr[I], num_arr[I])
        
        maximo = max(suma_actual, maximo)

    # hago suma de prefijos para contar arreglos con cierta propiedad
    acumulado = 0
    acumulados_pasados = {}
    acumulados_pasados[0] = 1
    ocurrencias = 0 

    for num in num_arr:
        # acumulado para las sumas parciales entre el comienzo
        # y la posición actual
        acumulado += num
        diferencia = acumulado - maximo 
        
        # si existe una diferencia en acumulados pasados quiere decir
        # que ya existe un acumulado que junto al acumulado actual
        # obtenemos el máximo
        if diferencia in acumulados_pasados: 
            ocurrencias += acumulados_pasados[diferencia] 

        # registramos los acumulados y contamos cuantas veces aparecen
        # esto nos dará el número de subarreglos si llegara a existir
        # una diferencia que con el acumulado nos da el máximo
        if acumulado in acumulados_pasados: 
            acumulados_pasados[acumulado] += 1
        else:
            acumulados_pasados[acumulado] = 1
    
    rta.append("{} {}".format(maximo, ocurrencias))

stdout.write("\n".join(rta) + "\n")