# p071-suma-promedio-numeros.py
# Calcula la suma y le promedio n calificaciones

while True:
    print('\033[2J\033[H', end='')
    print('Calcula la suma y le promedio n calificaciones\n')
    n = int(input('Cuantas calificaicones ? '))
    suma = 0
    strcals =''
    for i in range(1, n+1, 1):
        cal = int(input(f'Calificacion {i} : '))
        suma += cal
        strcals = strcals + str(cal) + ''

    print(f'\nLos numeros fueron: {strcals}')
    print(f'\nLa suma es : {suma}')
    print(f'El promedio es : {suma/n}')

    if input('\nSeguimos (S/N)?').upper()=='N':break
