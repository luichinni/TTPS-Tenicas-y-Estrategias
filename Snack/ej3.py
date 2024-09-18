from sys import stdin

precios = (4.00,4.50,5.00,2.00,1.50)

for linea in stdin:
    valores = linea.split(' ')
    
    total = precios[int(valores[0])-1] * float(valores[1])
    
    print(f'Total: R$ {total:.2f}')
    