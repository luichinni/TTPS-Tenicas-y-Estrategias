from sys import stdin, stdout

def max_sum_sq(nums: list):
    """
    Uso algoritmo de Kadane pero modificado
    Resultado: no está bien, WA
    """
    # agrego esto para que no falle si el ult elem es valido
    max_sum = -float('inf') # Incializo maximo en -infinito
    ocurrencias = 0 # cantidad de veces que encuentro al maximo
    suma_actual = 0 # suma acumulada actual
    
    for num in nums:
        """
        Por cada numero en el arreglo de entrada pasan 2 cosas
            1. si sumarlo al conteo actual es mayor al numero actual, lo agrego efectivamente
            2. sino, tomo como nuevo acumulado al numero actual

        Ahora, si la suma actual es mayor al maximo se establece el nuevo maximo y reinicio el contador
        si la suma actual es igual al maximo entonces le sumo 1 a las ocurrencias de subarreglos que contengan al maximo
        """
        if suma_actual + num > num:
            suma_actual += num
        else:
            suma_actual = num
                
        if suma_actual > max_sum:
            max_sum = suma_actual
            ocurrencias = 1
        elif suma_actual == max_sum:
            ocurrencias += 1 
        
    return "{} {}".format(max_sum, ocurrencias)

rta = []

casos = int(stdin.readline())
for _ in range(casos):
    stdin.readline() # numero de elementos en el array (en python no lo necesito)
    arr = [int(elem) for elem in stdin.readline().split(" ")]

    rta.append(max_sum_sq(arr))

stdout.write("\n".join(rta) + "\n")