from math import sqrt
from sys import stdin, stdout

"""
Factorización prima, representar cualquier numero como producto de nros primos.
https://www.youtube.com/watch?v=a3lp2u_52nQ

Formula de Polignac o de Legendre, factorización prima de un factorial.
https://es.wikipedia.org/wiki/F%C3%B3rmula_de_De_Polignac

Usando esto es posible saber si un factor aparece o no en la factorización del factorial,
para que un número divida a un factorial, todos sus factores primos (p^k) deben ser 
menor o igual a los factores del factorial (redundancia is my passion).
"""

def criba() -> list:
    """
    Genero la criba desde 2 hasta un nro arbitrario para no buscar maximos ni raices
    """
    limite = 50000
    criba = [True] * (limite + 1)
    criba[0], criba[1] = False, False # 0 y 1 no son primos

    primos = []

    for num in range(2, limite + 1): # +1 para procesar "limite"
        if criba[num]: # si aun se considera primo
            primos.append(num)

            for multiplo in range(num * num, limite + 1, num):
                """
                num * num -> inicia en num^2 ya que si num es primo, todos los nros entre
                            num *2 y num * num ya fueron marcados.
                """
                criba[multiplo] = False

    return primos

def factores_primos(primos:set, valor: int) -> dict:
    """
    Factorización prima de un valor dado, el diccionario de retorno seria algo asi
    ```
    {
        nro_1: exponente_1,
        ... ,
        nro_n: exponente_n
    }
    ```
    """
    factores = {}
    cociente = valor

    for divisor in primos:
        if divisor * divisor > cociente:  # Solo es necesario revisar hasta la raíz cuadrada
            break

        while cociente % divisor == 0:  # Dividir mientras se pueda por el mismo primo
            cociente //= divisor  # División entera
            factores[divisor] = factores.get(divisor, 0) + 1

    # Si después de todo eso el cociente sigue siendo mayor que 1, se asume que es primo
    if cociente > 1:
        factores[cociente] = factores.get(cociente, 0) + 1

    return factores

def factorial_divisible_por_factores(factores: dict, n: int, factorizado: int) -> bool:
    """
    Se toma la factorización hecha y se busca de cada p^k si es menor igual al factor del valor dado,
    siendo el valor, el factorial ```n!```
    """
    if not factores: # si no hay factores no es divisible
        return False
    
    for base, exp in factores.items(): # factores son los factores primos base, exp de un numero dado
        factor_primo = 0
        for K in range(1, exp+1):
            factor_primo += n // (base ** K) # div entera de n / p^k, el resultado es cuantas veces aparece

        if factor_primo < exp: # si el factor primo (exp del factor en n!) es menor al exponente del factor del divisor, significa q no lo divide
            return False

    return True

lines = [[int(data) for data in line.split()] for line in stdin.readlines()]

primos = criba() # primos con nro arbitrario para no buscar el divisor más grande, eso consumia mucho tiempo

rta = []

for line in lines:
    factores = factores_primos(primos, line[1])

    """
    Input es n! divisor
    si n es 0 y divisor es 1, entonces 0! = 1 => 1/1 True
    si divisor es 1 o 0, pueden dividir a todos ya que algo/1 = algo y algo/0 = indeterminado pero lo consideramos True
    """
    if (line[0] == 0 and line[1] == 1) or (line[1] == 1) or (line[1] == 0) or factorial_divisible_por_factores(factores, line[0], line[1]):
        rta.append("{} divides {}!".format(line[1], line[0]))
    
    else:
        rta.append("{} does not divide {}!".format(line[1], line[0]))

stdout.write("\n".join(rta) + "\n")