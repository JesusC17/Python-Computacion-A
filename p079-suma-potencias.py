# p079-suma-potencias.py
# Suma las potencias de un numero x desde x^1 ...... x^n

print('\033[2J\033[H', end='')
print(f'Calculando la serie de S = x^1 ...... x^n \n')

x = int(input('Numero base x : '))
n = int(input('Cuantos terminos n: '))
suma = 0


print('S = ', end='')
for i in range(1, n+1):
    ta = 1
    for j in range(i):
        ta = ta * x
    print(f"{x}^{i} {'+' if i<n else ''} ", end='')
    suma += ta
print(f'= {suma:,}')
