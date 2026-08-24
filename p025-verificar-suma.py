# p025-verificar-suma.py
# Dados tres numeros enteros verifica si la suma de los dos primeros es igual al tercero

print("\033[2J\033[H", end="")
print('Dados tres numeros enteros verifica si la suma de los dos primeros es igual al tercero\n')

n1 = int(input('Numero 1: '))
n2 = int(input('Numero 2: '))
n3 = int(input('Numero 3: '))

if n1 + n2 == n3:
    print(f' {n1} + {n2} = {n3} Son IGUALES ')
else:
    print(f' {n1} + {n2} != {n3} Son DIFERENTES')

print('\nFin del programa')