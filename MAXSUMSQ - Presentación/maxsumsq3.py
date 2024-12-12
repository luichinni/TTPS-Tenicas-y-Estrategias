from sys import stdin, stdout

rta = []

tests = int(stdin.readline())

for _ in range(tests):
    tam_arr = int(stdin.readline())

    num_arr = [int(elem) for elem in stdin.readline().split()]

    maximo = num_arr[0]
    suma_actual = num_arr[0]
    sumas = {}
    sumas[num_arr[0]] = 1

    for I in range(1,tam_arr):
        # busco la suma maxima de subsecuencia, algoritmo de kadane
        suma_actual = max(suma_actual + num_arr[I], num_arr[I])
        
        # registro los maximos para luego buscar cual tiene más ocurrencias
        if suma_actual > maximo:
            maximo = suma_actual
            sumas[maximo] = 1
        elif suma_actual == maximo:
            sumas[maximo] += 1
            
    max_count = 1
    for sum_val, count in sumas.items():
        if count > max_count:
            max_count = count
            maximo = sum_val

    rta.append("{} {}".format(maximo, max_count))

stdout.write("\n".join(rta) + "\n")