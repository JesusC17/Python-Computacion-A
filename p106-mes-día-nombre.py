# p106-mes-día-nombre.py
# Lee un numero de mes (ej 4). Imprime el numero de mes y la cantidad de dias del mes correspondiente

Nombres = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
Dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Leer numero de mes' + '\033[0m')

try:
    mes = int(input('Introduzca un numero de mes (1 - 12): '))
    if mes < 1 or mes > 12:
        print('Nota invalida. Ingresa dato dentro del rango (1 - 12).')
    else:
        print('--- Resultados ---')
        print('Mes: ', Nombres[mes - 1])
        print('Días: ', Dias[mes - 1])
except ValueError:
    print('Nota invalida. Ingresa dato dentro del rango (1 - 12).')

