# p047-conteo-descendente-v2.py
# Imprimir los numeros de n a 1, en intervalos de m


print('\033[2J\033[H', end='')
print('Imprimir los numeros de n a 1, en intervalos de m usando while')

n = int(input('Desde donde? '))
m = int(input('Decrementos? '))


c = n

while c >= 1:
    print(f'{c} ', end='')
    c-=m

print('\nProceso terminado ', c)