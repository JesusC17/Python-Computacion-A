# p014-funciones-trigonometricas.py
# Ejemplo de uso de funciones trigonometricas y conversion de grados

import math as mt

print("\033[2J\033[H", end="")
print('Ejemplo de uso de funciones trigonometricas y conversion de grados \n')

angulo = int(input('Dame un angulo en grados: '))
radianes = mt.radians(angulo)

seno    = mt.sin(radianes)
coseno  = mt.cos(radianes)
tangente= mt.tan(radianes)

grados = mt.degrees(radianes)

salida = ('Resumen de funciones trigonometricas y de conversion\n'
f'El seno es        {seno:.4f} \n'
f'El coseno es      {coseno:.4f} \n'
f'La tangente es    {tangente:.4f} \n'
f'El angulo de {grados} grados, equivale a {radianes:.4f} radianes'
)

print(salida)