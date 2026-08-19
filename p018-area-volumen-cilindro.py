# p018-area-volumen-cilindro.py
# Programa que calcula el area y volumen de un cilindro

import math as mt

print("\033[2J\033[H", end="")
print('Programa que calcula el area y volumen de un cilindro \n')

R = float(input('Ingresa el radio: '))
h = float(input('Ingresa el altura: '))

# area = 2 * mt.pi * (R + h)    
area = 2 * mt.pi * R * (R + h)
volumen = mt.pi * R**2 * h

print(f'El area del cilindro es:    {area:.2f}\n')
print(f'El volumen del cilindro es: {volumen:.2f}\n')