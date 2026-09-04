# p059-pares-descendente.py
# Imprime y suma los numeros pares en un rango descendente desde 100 hasta n

print('\033[2J\033[H', end='')
print('Imprime y suma los numeros pares en un rango descendente desde 100 hasta n')

while True:
    print('\033[2J\033[H', end='')
    n = int(input('Introduce un numero limite (menor a 100): '))
    suma = 0
    c = 100
    print('Numeros pares: ', end='')
    while c >= n:
        if c % 2 == 0:
            print(f'{c}, ', end='')
            suma += c
        c -= 1
    
    print(f'\nLa suma de los pares es: {suma} ')

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break    
print('\nTerminamos...')