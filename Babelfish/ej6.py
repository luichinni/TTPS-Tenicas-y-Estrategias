from sys import stdin

linea = input()

dicc = {}

while(linea.rstrip() != ''):
    palabra, traduccion = linea.split(' ')
    dicc[traduccion] = palabra
    linea = input()

mensaje = ''

for line in stdin:
    line = line.rstrip()
    if (line in dicc.keys()):
        mensaje += dicc[line] + '\n'
    else:
        mensaje += 'eh\n'

print(mensaje.rstrip())
