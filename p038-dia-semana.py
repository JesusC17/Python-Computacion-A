# p038-dia-semana.py
# Programa que imprime el dia segun el numero ingresado de 1 a 7, siendo 1 domingo

print('\033[2J\033[H', end='')
print('Programa que imprime el dia segun el numero ingresado de 1 a 7, siendo 1 domingo')

dia = int(input('Ingresa el nuumero de dia: '))

if dia < 1 or dia > 7:
    print('\nIngresa un dato valido')
else:
    if dia == 1:
        print('EL dia es Domingo')
    elif dia == 2:
        print('EL dia es Lunes')
    elif dia == 3:
        print('EL dia es Martes')
    elif dia == 4:
        print('EL dia es Miercoles')
    elif dia == 5:
        print('EL dia es Jueves')
    elif dia == 6:
        print('EL dia es Viernes')
    else:
        print('EL dia es Sabado')
        