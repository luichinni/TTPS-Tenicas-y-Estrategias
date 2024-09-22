from sys import stdin

def is_valid_queue(inside: list, v_out:int)->bool:
    if (inside[0] == v_out):
        inside.pop(0)
        return True
    return False

def is_valid_stack(inside: list, v_out:int)->bool:
    if (inside[-1] == v_out):
        inside.pop()
        return True
    return False

def is_valid_p_queue(inside: list, v_out:int)->bool:
    m = max_index(inside)
    if (inside[m] == v_out):
        inside.pop(m)
        return True
    return False

def max_index(arr: list):
    maximo = -1
    indice = -1
    for indx in range(len(arr)):
        if (arr[indx] > maximo):
            maximo = arr[indx]
            indice = indx
    return indice
    

msg = ['queue','stack','priority queue']

comparator = ''



for linea in stdin:
    casos = int(linea)

    estructura = [True] * 3

    contador = 3

    structs = [[],[],[]]

    I = 0

    while (I < casos and contador > 0):
        cmd, valor = input().split(' ')
        cmd = int(cmd)
        valor = int(valor)
        if cmd == 1:
            for K in range(3):
                if estructura[K]: structs[K].append(valor)
        else:
            estructura = [
                estructura[0] and len(structs[0])>0 and is_valid_queue(structs[0],valor),
                estructura[1] and len(structs[1])>0 and is_valid_stack(structs[1],valor),
                estructura[2] and len(structs[2])>0 and is_valid_p_queue(structs[2],valor)
            ]
            contador = estructura.count(True)

        I+=1
    
    for J in range(casos - I):
        input()

    if contador > 1:
        comparator += 'not sure\n'
    elif contador == 0:
        comparator += 'imposible\n'
    else:
        comparator += msg[estructura.index(True)]+'\n'

print(comparator)