# p052-tabla-conversion.py
# Imprime una tabla de conversion de peso a dolar

tc = 16.80   #Cmbio actual de peso a dolar

while True:
    print('\033[2J\033[H', end='')
    print('Tabla de conversion de peso a dolar\n')
    print(f'Tipo de cambio: {tc}')
    print('-' * 40)

    while True: #Valida que valores de inicial y fianl sean correctos
        inicial = float(input('Valor inicial del rango? '))
        final = float(input('Valor final del rango? '))
        if inicial < final and inicial > 0 and final > 0: break
        else: print('Error. Inicial debe ser menor a final')

    c = inicial
    print('\nPeso\t\tDolar')
    print('-' * 30)
    while c <= final:
        print(f'{c:>10.2f} {c/tc:>10.2f}')
        c += 1
    print('-' * 30)

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break

print('\nTerminamos de imprimir las tablas...')