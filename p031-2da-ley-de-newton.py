# p031-2da-ley-de-newton.py
# Calcular los valores de la segunda ley de Newton

print("\033[2J\033[H", end="")
print('Calcular los valores de la segunda ley de Newton')

print('[ F ] uerza      (f = m * a )')
print('[ M ] asa        (m = f / a)')
print('[ A ] celeracion (f = f / m )')
print('Elige? ')

op = input().upper()  #Convierte a mayuscula

if op == 'F':
    print('\nCalculando la Fuerza')
    m = float(input('Dame la masa:  '))
    a = float(input('Dame la aceleracion:  '))
    f = m * a
    print('\n La fuerza es: ' + str(f))
elif op == 'M':
    print('\nCalculando la Masa')
    f = float(input('Dame la fuerza:  '))
    a = float(input('Dame la aceleracion:  '))
    m = f / a
    print('\n La masa es: ' + str(m))
elif op == 'A':
    print('\nCalculando la Aceleracion')
    f = float(input('Dame la fuerza:  '))
    m = float(input('Dame la masa:  '))
    a = f / m
    print('\n La aceleracion es: ' + str(a))
else:
    print('\nOpcion INCORRECTA')

print('\n Proceso terminado')
    