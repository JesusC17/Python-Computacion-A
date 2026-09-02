# p055-tabla-multiplicar-while-v2.py
# Imprime las tablas del 1 al 10, hasta el 10


while True:
    print('\033[2J\033[H', end='')
    print('Imprime las tablas del 1 al 10, hasta el 10\n')

    n = int(input('Hasta cual tabla quieres? '))
    m = int(input('Hasta donde llega? '))

    t = 1
    while t <= n:
        print(f'Tabla del {t} \n')
        c = 1
        while c <= m:
            print(f'{t:2} x {c:2} = {c*t}')
            c += 1
        t += 1


    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break

print('\nTerminamos de imprimir las tablas...')