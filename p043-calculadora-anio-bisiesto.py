# p043-calculadora-anio-bisiesto.py
# Programa que calcula si un año es bisiesto

print('\033[2J\033[H', end='')
print('Programa que calcula si un año es bisiesto. ')

anio = int(input('Ingresa el año: '))

if anio % 4 == 0 and not(anio % 100 == 0):
    print(f'El año {anio} SI bisiesto')
elif anio % 400 == 0:
    print(f'El año {anio} SI es bisiesto')
else:
    print(f'El año {anio} NO es bisiesto')
