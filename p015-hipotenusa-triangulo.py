# p015-hipotenusa-triangulo.py
# programa que calcule la longitud de la hipotenusa de un triángulo rectángulo.

import math as mt

print("\033[2J\033[H", end="")
print('Programa que calcula la hipotenisa de un triangulo rectangulo en base a sus catetos\n')

catA = float(input('Ingresa longitud del cateto a: '))
catB = float(input('Ingresa longitud del cateto b: '))

hipotenusa = mt.sqrt(  catA * catA + catB * catB)

print(f'La longitud de la hipotenusa del triangulo es: {hipotenusa:.2f}')