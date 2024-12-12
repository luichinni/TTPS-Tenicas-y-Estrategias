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
    aparecidos = {}
    aparecidos[0] = 1
    ocurrencias = 0

    for num in num_arr:
        acumulado += num
        diferencia = acumulado - maximo
        
        if diferencia in aparecidos:
            ocurrencias += aparecidos[diferencia]

        if acumulado in aparecidos:
            aparecidos[acumulado] += 1
        else:
            aparecidos[acumulado] = 1

    rta.append("{} {}".format(maximo, ocurrencias))

stdout.write("\n".join(rta) + "\n")