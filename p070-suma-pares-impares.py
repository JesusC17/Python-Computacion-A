# p070-suma-pares-impares.py
# Imprime numeros pares o impares de 1 a n segun lo decida 

print('\033[2J\033[H', end='')
print('Imprime numeros pares o impares de 1 a n segun lo decida\n')

print('[1] Voy de 1 a n con pares')
print('[2] Voy de 1 a n con impares')
op = int(input('Elige ? '))
suma = 0
if op == 1:
    print('Vamos de 1 a n con pares')
    n = int(input('Hasta donde ?'))
    for x in range (2, n+1, 2):
        print(f'{x} ', end='')
        suma += x
    print('Suma = '+ str(x))
elif op == 2:
    print('Vamos de 1 a n con impares')
    n = int(input('Hasta donde ?'))
    for x in range (1, n+1, 2):
        print(f'{x} ', end='')
        suma += x
    print('Suma = '+ str(x))
    
else:
    print('\nOpcion Erronea')

    print('\n\nProceso Terminado')
