# p045-conteo-ascendente-v2.py
# Imprimir numeros de 1 a n usando while


print('\033[2J\033[H', end='')
print('Imprimir numero de 1 a 100 usando while')

n = int(input('Hasta donde? '))
m = int(input('Incrementos? '))

c = 1
while c <= n:
    print(f'{c} ', end='')
    c += m

print(f'\nProceso terminado: {c}')