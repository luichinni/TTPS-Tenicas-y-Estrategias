from sys import stdin

def salida_valida_cola(values: list, out: int) -> bool:
    pude = False
    if values[0] == out:
        values.remove(values[0])
        pude = True
    return pude

def salida_valida_pila(values: list, out: int) -> bool:
    pude = False
    ultimo = values.pop()
    if ultimo == out:
        pude = True
    return pude

msg = ['stack','queue','priority queue']

for linea in stdin:
    estructuras = [True] * 3

    v_in = {
        'pila': [],
        'cola': [],
        'p_cola': []
    }

    casos = int(linea)

    for I in range(casos):
        instruccion, value = input().split(' ')
        value = int(value)
        instruccion = int(instruccion)

        if instruccion == 1:
            for estructura in v_in:
                v_in[estructura].append(value)
        else:
            v_in['p_cola'].sort(reverse=True)

            if estructuras[0] == True:
                estructuras[0] = estructuras[0] and salida_valida_pila(v_in['pila'],value)
            if estructuras[1] == True:
                estructuras[1] = estructuras[1] and salida_valida_cola(v_in['cola'],value)
            if estructuras[2] == True:
                estructuras[2] = estructuras[2] and salida_valida_cola(v_in['p_cola'],value)

    if estructuras.count(True) > 1:
        print('not sure')
    elif (estructuras.count(True) == 0):
        print('impossible')
    else:
        print(msg[estructuras.index(True)])
print('\n')