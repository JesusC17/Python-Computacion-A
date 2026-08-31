#p044-conteo-ascendente.py
# Imprimir numeros de 1 a n usando while


print('\033[2J\033[H', end='')
print('Imprimir numero de 1 a 100 usando while')

c = 1
while c <= 100:
    print(f'{c} ', end='')
    c += 1

print(f'\nProceso terminado: {c}')