from sys import stdin, stdout

def mul(num_arr: list):
    result = 1
    for num in num_arr:
        result *= num

    return result

def coef_binomial(n, r):
    tabla = [[0] * (n+1) for _ in range(n+1)]

    for I in range(n+1):
        tabla[I][0] = 1
        tabla[I][I] = 1
    
    for I in range(1, n+1): # arranca de 1 porq ya estan cubiertos los casos base
        for J in range(1, I): # extremos tambien ya estan cubiertos
            tabla[I][J] = tabla[I-1][J-1] + tabla[I-1][J]

    return tabla[n][r]

stdin.readline()

rta = []

for line in stdin:
    K, B = tuple([int(num) for num in line.split(' ')])

    chocolates = 0
    for box in range(B):
        chocolates += mul([int(num) for num in stdin.readline().split(' ')])

    rta.append(str(coef_binomial(chocolates, chocolates // K)))

stdout.write("\n".join(rta) + "\n")