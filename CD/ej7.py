from sys import stdin

lineas = stdin.readlines()

I = 0

while (I < len(lineas) and True):
    jack_cant, jill_cant = map(int,lineas[I].split())
    I+=1

    if (jack_cant == 0 and jill_cant == 0):
        break
    elif (jack_cant == 0 or jill_cant == 0):
        print(0)
        I+=jack_cant
        I+=jill_cant
    else:

        jack_cd = set()
        for J in range(jack_cant):
            nro_cd = int(lineas[I])
            I+=1
            jack_cd.add(nro_cd)
        
        ultimo = int(lineas[I-1])

        contador = 0
        J = 0
        cd_actual = -1
        while (J < jill_cant and cd_actual < ultimo):
            cd_actual = int(lineas[I])
            I+=1
            if (cd_actual in jack_cd):
                contador+=1
            J+=1

        I += (jill_cant - J)

        print(contador)
