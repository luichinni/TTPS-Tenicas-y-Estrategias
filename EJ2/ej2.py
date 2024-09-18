from sys import stdin
from math import floor

dias = ('Su','Mo','Tu','We','Th','Fr','Sa')
no_laborable = ('Fr','Sa')

"""
2   -> 1st line; n of test cases
14  -> days of 1st test
3   -> n of political parties
3   -> h1
4   -> h2
8   -> h3
100 -> days of 2nd test
4   -> n of political parties
12  -> h1
15  -> h2
25  -> h3
40  -> h4
"""

def calcular_dias(dias_sim: int, hartal_params: list[int]) -> int:
    dias_paro = set([])

    for h_param in hartal_params:
        for dia in range(0,dias_sim+1,h_param): #arranca en cero porq sino cuenta el dia 1 SIEMPRE
            day_index = dia % 7
            if day_index == 0: day_index = 7
            if (not (dias[day_index-1] in no_laborable)):
                dias_paro.add(dia)
    
    return len(dias_paro)


casos = int(input())
for I in range(0,casos):
    dias_sim = int(input())
    cant_partidos = int(input())

    hartal_params = []

    for K in range(0,cant_partidos):
        hartal_params.append(int(input()))

    print(calcular_dias(dias_sim, hartal_params))