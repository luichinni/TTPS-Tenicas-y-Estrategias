"""
Input es
1. num T de cantidad de casos
2. cantidad n nros en primer array
3. array separado por espacios con cada Ai
<-> se repite hasta 2*T lineas <->

Donde:
1 <= T <= 35 (max 35 casos)
1 <= n <= 100000 (max 100k numeros por array)
-1000 <= Ai <= 1000 (los nros del array van desde -10k hasta 10k)

Output:
Por cada caso imprimir separado por espacios, el nro maximo sumado consecutivo y la cantidad de veces
que aparece

nro_maximo_sumado cant_veces_calculado
"""
from sys import stdin, stdout

class Maximo:
    def __init__(self):
        # maximo 1 por debajo del minimo posible
        self.max_sum = -1000000001
        self.cantidad = 0

    def comprobar(self, value):
        if value > self.max_sum:
            self.max_sum = value
            self.cantidad = 1
        elif value == self.max_sum:
            self.cantidad += 1

    def get_rta(self):
        return "{} {}".format(self.max_sum, self.cantidad)


def max_sum_sq(nros):
    sumas = []
    m = Maximo()

    for nro in nros:
        for I in range(len(sumas)):
            # sumas acumuladas
            sumas[I] += nro
            m.comprobar(sumas[I])
        
        m.comprobar(nro)
        sumas.append(nro)
    
    return m.get_rta()


casos = int(stdin.readline())

rta = []

for _ in range(casos):
    stdin.readline() # nos quitamos la cant de nros en el array

    numeros = [int(nro) for nro in stdin.readline().split(" ")]

    rta.append(max_sum_sq(numeros))

stdout.write("\n".join(rta) + "\n")