# p053-conjetura-collatz.py
# Imprime la conjetura de Collatz
# Dado n, si es par n / 2, si es impar 3 * n + 1 hasta llegar a 1

while True:
    print('\033[2J\033[H', end='')
    print('Imprime los numeros de la conjetura de Collatz')
    n = int(input('Dame un numero entero positivo: '))
    while n != 1:
        print(f'{n} ', end='')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n)
    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break

print('\nTerminamos de imprimir las tablas...')
