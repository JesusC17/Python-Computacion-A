# p054-tabla-multiplicar-while-v1.py
# Imprime la tabla t de 1 a 10, usando while

while True:
    print('\033[2J\033[H', end='')
    print('Imprime la tabla t de 1 a 10, usando while\n')

    t = int(input('Que tabla quieres ? '))
    n = int(input('Hasta donde ? '))

    print(f'Imprimiendo la tabla del {t}')

    c = 1
    while c <= n:
        print(f'{t:2} x {c:2} = {c*t}')
        c += 1
        
    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break
    
    print('\nTerminamos de imprimir las tablas...')
