# p082-cuadro-hueco-caracter.py
#

print('\033[2J\033[H', end='')
print('Programa que imprime un cuadrado de dimensiones dadas con caracter ingresado \n')

lado = int(input('De que tamaño sera el lado del cuadrado? '))
c = input('Que caracter quieres usar? ')

for i in range(1, lado + 1):
    for j in range(1, lado + 1):
        if i == 1 or i == lado:
            print(f'{c} ',end='')
        else:
            if j == 1 or j == lado:
                 print(f'{c} ', end='')
            else:
                print('  ', end='')
    print()