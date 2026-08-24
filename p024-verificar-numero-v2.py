# p024-verificar-numero-v2.py
# Programa que verifica si un numero es 0, positivo o negativo

print("\033[2J\033[H", end="")
print('Programa que verifica si un numero es 0, positivo o negativo V2\n')

numero = int(input('Ingresa el numero a verificar: '))

if numero > 0:
    print('El numero es POSITIVO 👍')
else: 
    if numero < 0:
        print('El numero es NEGATIVO 👎')
    else:
        if numero == 0:
            print('El numero es CERO 😁')

print('\nAqui termina el programa')
