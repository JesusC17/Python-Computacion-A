# p061-suma-200.py
# Lee numeros y los suma hasta que acumulen 200 o mas, al terminar meustra cuantos numeros s e introdujeron y la suma final

while True:
    print('\033[2J\033[H', end='')
    print(' Lee numeros y los suma hasta que acumulen 200 o mas, al terminar meustra cuantos numeros s e introdujeron y la suma final\n')
    suma = c =0
    while True:
        print(f'Suma actual: {suma}.')
        n = int(input('Introduce un numero: '))
        c += 1
        suma += n
        if suma >= 200: break

    print('-' * 30)
    print('Meta de 200 alcanzada.')
    print(f'Suma final: {suma}')
    print(f'Total de numeros introducidos: {c}')

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break    
print('\nTerminamos...')
