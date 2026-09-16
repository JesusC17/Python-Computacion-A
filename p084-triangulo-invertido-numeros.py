# p084-triangulo-invertido-numeros.py
# Programa que imprime un triangulo invertdo de n renglones

print('\033[2J\033[H', end='')
print('Programa que imprime un triangulo invertdo de n renglones \n')

n = int(input('Ingresa el numero: '))
v = 1

for j in range(1, n+1):
    v = 1
    for i in range(1, n+1):
        if i >= j:
            print(f'{v} ', end='')
            v += 1
    print()