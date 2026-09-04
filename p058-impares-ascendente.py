# p058-impares-ascendente.py
# Imprime y suma los numeros primos en un rango de 1 a uno introducido por el usuario

print('\033[2J\033[H', end='')
print('Imprime y suma los numeros primos en un rango de 1 a uno introducido por el usuario\n')

while True:
    print('\033[2J\033[H', end='')
    n = int(input('Introduce un numero limite: '))
    suma = 0
    c = 1
    print('Numeros impares: ', end='')
    while c <= n:
        if not c % 2 == 0:
            print(f'{c}, ', end='')
            suma += c
        c += 1

    print(f'\nLa suma de los impares es: {suma} ')

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break

print('\nTerminamos...')