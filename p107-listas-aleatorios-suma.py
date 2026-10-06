# p107-listas-aleatorios-suma.py
# Genera 2 listas aleatorias cada una. Se crea una tercera lista dond el elemento
# es la suma de lo correspondiente en la lista A y B, solo si ambos son impares, sino es 0
# imprime las 3 listas

import random

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Lista aleatorias con suma' + '\033[0m')

lista_a = [random.randint(1, 20) for i in range(10)]
lista_b = [random.randint(1, 20) for i in range(10)]
lista_c = []

for a, b in zip(lista_a, lista_b):
    if a % 2 != 0 and b % 2 != 0:
        lista_c.append(a + b)
    else:
        lista_c.append(0)

print('--- Listas Generadas ---')
print('Lista A: ',lista_a)
print('Lista B: ',lista_b)

print('--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---')
print('Lista C: ', lista_c)