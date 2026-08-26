# p037-numero-mayor.py
# Programa que lee 3 numeros e identifica al mayor

print('\033[2J\033[H', end='')
print('Programa que lee 3 numeros e identifica al mayor')

print('Ingresa los tres numeros separados por espacio: ')
n1, n2, n3 = map(int, input().split())

if n1 == n2 and n1 == n3:
    print('Los numeros son iguales')
elif n1 >= n2 and n1 >= n3:
    print(f'El mayor es: {n1}')
elif n1 <= n2 and n2 >= n3:
    print(f'El mayor es: {n2}')
else:
    print(f'El mayor es: {n3}')
