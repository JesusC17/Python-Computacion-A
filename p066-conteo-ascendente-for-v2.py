# p066-conteo-ascendente-for-v2.py
# Imprime numeros de 1 a n en intervalos de m

print('\033[2J\033[H', end='')
print('Imprime numeros de 1 a n en intervalos de m usando for\n')

n = int(input('Hasta donde  ? '))
m = int(input('Intervalos   ? '))
 
for i in range (1, n+1, m):
    print(i)
