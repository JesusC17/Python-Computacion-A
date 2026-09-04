# p060-promedio-suma.py
# Lee numeros introducidos por el usuario hasta ingresar un 0, al finalizar muestra el conteo, la suma y promedio de la serie


while True:
    print('\033[2J\033[H', end='')
    c = suma = 0
    print('Introduce numeros (0 para terminar)')
    while True:
        n = int(input('> '))
        if n == 0: break
        c += 1
        suma += n

    promedio = suma / c
    print(f'Se introdujeron {c} numeros.')
    print(f'La suma es: {suma}')
    print(f'El promedio es: {promedio:.1f}')

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break    
print('\nTerminamos...')