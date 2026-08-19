# p021-distancia-entre-puntos.py
# Programa que calcula distancia entre dos puntos

import math as mt

print("\033[2J\033[H", end="")
print('Programa que calcula la distancia entre dos puntos en un plano cartesiano \n')

print('Dame coordenadas de punto A separadas por coma: ')
x1, y1 = input().split(",")
x1, y1 = int(x1), int(y1)
print('\nDame coordenadas de punto B separadas por coma: ')
x2, y2 = input().split(",")
x2, y2 = int(x2), int(y2)

distancia = mt.sqrt( (mt.pow((x2 - x1), 2)) + (mt.pow((y2 - y1), 2)))

print(f'La distancia entre el punto A y B es de: {distancia:.2f}')