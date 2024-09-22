from sys import stdin

linea = input()

dick = {}

while(linea.rstrip() != ''):
    palabra, traduccion = linea.split(' ')
    dicc[traduccion] = palabra
    linea = input()

mensaje = ''

for line in stdin:
    line = line.rstrip()
    if (line in dick.keys()):
        mensaje += dick[line] + '\n'
    else:
        mensaje += 'eh\n'

print(mensaje.rstrip())
