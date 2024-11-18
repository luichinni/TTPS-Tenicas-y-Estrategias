from sys import stdin, stdout

def binary_exp(base, decimal_exp, divisor):
    res = 1
    while (decimal_exp != 0): # mientras aun queden bits por verificar, itera
        if decimal_exp % 2 == 1: # si el resto es 1 significa que es un bit que nos importa operar
            res = (res * base) % divisor # el resultado se multiplica por la base y usando la prop del modulo, se busca el resto en cada paso
        
        base = (base * base) % divisor # se modifica la base en cada paso
        decimal_exp //= 2 # division por 2 para ir desarmando el exp en binario

    return res

lineas_in = [[int(dato) for dato in linea.split(' ')] for linea in stdin.readlines()]

rta = []

for linea in lineas_in[1:-1]:
    rta.append(str(binary_exp(*linea)))

stdout.write("\n".join(rta) + "\n")