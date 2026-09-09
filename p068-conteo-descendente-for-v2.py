# p068-conteo-descendente-for-v2.py
# Imprime numeors de n a 1 en decrementos de 1 en intervalos de m usando for

print('\033[2J\033[H', end='')
print('Imprime numeors de n a 1 en decrementos de 1 en intervalos de m usando for\n')

n = int(input('Desde donde ?'))
m = int(input('Intervalos  ?'))

for i in range(n, 0, -m):
    print(i)

print('\nProceso Terminado')