# p012-funcion-matematicas-equacion.py
# Ejemplifica el uso de funciones de matemaicas dentro math
# Evaluar la funcion f(x,y)

import math as mt

print("\033[2J\033[H", end="")
x = float(input('x = '))
y = float(input('y = '))

fxy = 3 * mt.pow(x, 2) + mt.sqrt( mt.pow(x, 2) + mt.pow(y, 2) ) + mt.exp( mt.log(x) )
fxy2 = 3 * x ** 2 + mt.sqrt( x**2 + y**3 ) + mt.exp( mt.log(x) )

print(f'El resultado es : {fxy:,.2f}')
print(f'El resultado es : {fxy2:,.2f}')