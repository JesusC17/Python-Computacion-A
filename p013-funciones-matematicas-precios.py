# p013-funciones-matematicas-precios.py
# Demostrar el uso de funciones matematicas de redondeo

import math as mt

print("\033[2J\033[H", end="")

precio = 15.65

print(f'Precio Original $ {precio:.2f}')
print(f'Arriba          $ {mt.ceil(precio):.2f}')
print(f'Abajo           $ {mt.floor(precio):.2f}')
print(f'Truncar         $ {mt.trunc(precio):.2f}')
print(f'Automatico      $ {round(precio):.2f}')
print(f'Automatico dec  $ {round(precio,3):.2f}')