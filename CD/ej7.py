from sys import stdin

lineas = stdin.readlines()

I = 0

mensaje = ''

while True:
    jack_cant, jill_cant = map(int,lineas[I].split())
    if (jack_cant == 0 and jill_cant == 0):
        break
    I+=1

    jack_idx = I
    jill_idx = I + jack_cant

    contador = 0
    while (jill_idx < (I+jack_cant+jill_cant) and jack_idx < (I+jack_cant)):
        jack_cd = int(lineas[jack_idx])
        jill_cd = int(lineas[jill_idx])
        if (jack_cd == jill_cd):
            contador+=1
            jill_idx+=1
            jack_idx+=1
        elif (jack_cd > jill_cd):
            jill_idx+=1
        elif (jack_cd < jill_cd):
            jack_idx+=1

    print(contador)
    I+=jack_cant+jill_cant