# p023-verificar-numero.py
# Programa que verifica si un numero es 0, positivo o negativo

print("\033[2J\033[H", end="")
print('Programa que verifica si un numero es 0, positivo o negativo \n')

numero = int(input('Ingresa el numero a verificar: '))

if numero > 0:
    print('El numero es POSITIVO 👍')
if numero < 0:
    print('El numero es NEGATIVO 👎')
if numero == 0:
    print('El numero es CERO 😁')

print('\nAqui termina el programa')
