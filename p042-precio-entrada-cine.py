# p042-precio-entrada-cine.py
# Programa que calcula el repcio de boleto de cine segun la edad

print('\033[2J\033[H', end='')
print('Programa que calcula el repcio de boleto de cine segun la edad')

edad = int(input('Ingresa la edad: '))

if edad < 5:
    print('La entrada es gratis')
elif edad <= 12:
    print('El precio del boleto es $5')
elif edad <= 64:
    print('El precio del boleto es $10')
else:
    print('El precio del boleto es $7')

