from sys import stdin

notas = {
    'W': 1.0,
    'H': 0.5,
    'Q': 0.25,
    'E': 0.125,
    'S': 0.0625,
    'T': 0.03125,
    'X': 0.015625
}

def count_right_measures(linea: str) -> int:
    contador = 0
    medidas = linea.split('/')
    
    for medida in medidas:
        if (medida != '' and is_right_measure(medida)):
            contador+=1
            
    return contador

def is_right_measure(measure: str) -> bool:
    tiempo = 0.0
    for I in range(0,len(measure)):
        tiempo = tiempo + notas[measure[I]]

    return tiempo == 1.0


for linea in stdin:
    linea = linea.replace('\n','')
    
    if (linea == "*"):
        break
    
    print(count_right_measures(linea))