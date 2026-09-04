# p063-numero-mayor.py
# Lee una serie de numeros hasta que se ingrese un 0, al final se imprime el numero mas grande introducido

print('\033[2J\033[H', end='')
print('Lee una serie de numeros hasta que se ingrese un 0, al final se imprime el numero mas grande introducido\n')

while True:
    nm = 0
    print('Introduce numeros (0 para terminar):')
    while True:
        n = int(input('> '))
        if n == 0: break
        if n > nm:
            nm = n
    print('-' * 50)
    print(f'El numero mayor fue: {nm}')
    if input('\nDeseas Continuar (S/N)? ').upper() == 'N': break    
print('\nTerminamos...')    