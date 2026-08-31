# p046-conteo-descendente.py
# Imprimeir los numeros de 100 a n


print('\033[2J\033[H', end='')
print('Imprimir los numeros de 100 a 1 usando while')

c = 100

while c >= 1:
    print(f'{c} ', end='')
    c-=1

print('\nProceso terminado ', c)