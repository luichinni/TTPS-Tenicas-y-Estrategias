from sys import stdin, stdout

def actualizar(nuevo, viejo, contador, aumento = 1):
    if nuevo > viejo:
        contador = 0
        viejo = nuevo
    elif nuevo == viejo:
        contador += aumento

    return (viejo, contador)

rta = []

tests = int(stdin.readline())

for _ in range(tests):
    tam_arr = int(stdin.readline())

    num_arr = [int(elem) for elem in stdin.readline().split()]

    maximo = -float("inf")
    suma_actual = 0
    contador = 0

    for I in range(0,tam_arr):
        # busco la suma maxima de subsecuencia, algoritmo de kadane
        # suma_actual = max(suma_actual + num_arr[I], num_arr[I])
        if suma_actual + num_arr[I] > num_arr[I]:
            suma_actual+=num_arr[I]
            maximo, contador = actualizar(suma_actual, maximo, contador)

        elif suma_actual + num_arr[I] == num_arr[I]:
            suma_actual = num_arr[I]
            maximo, contador = actualizar(suma_actual, maximo, contador, 2)

        else:
            suma_actual = num_arr[I]
            maximo, contador = actualizar(suma_actual, maximo, contador)


    rta.append("{} {}".format(maximo, contador))

stdout.write("\n".join(rta) + "\n")