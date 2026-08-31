# p049-sumar-consecutivos.py
# Suma numeros hasta que el total sea >= 100

print('\033[2J\033[H', end='')
print('Suma numeros hasta que el total sea >= 100\n')

c = 0
s = 0

while c <= 200:
    c += 1
    s += c
    print(f'{c} ')
    if s >= 100: break

print(f'La suma {s} despues de {c} numeros')
