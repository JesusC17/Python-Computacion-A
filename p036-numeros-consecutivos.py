# p036-numeros-consecutivos.py
# Programa que determina si tres numeros son consecutivos

print('\033[2J\033[H', end='')
print('Programa que determina si tres numeros son consecutivos')

print('Ingresa los tres numeros separados por espacio: ')
n1, n2, n3 = map(int, input().split())

if n2 - n1 == 1 and n3 - n2 == 1:
    print(f'Los numeros {n1}, {n2} y {n3} son consecutivos')
else:
    print('Los numeros no son consecutivos')