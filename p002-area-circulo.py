# p002-area-circulo.py
# Calcular el area de unn circulo

import math # importa la libreria de constantes y funciones amtematicas

print("Calculando el area de un circulo \n")

radio = float(input('Dame el radio ? '))

area = math.pi * radio ** 2
area = math.pi * math.pow(radio, 2)

print(f'El circulo de radio {radio}, tiene un area de {area:.2f}')
