# p104-procesar-notas.py
# Lee numero indeterminado de calificaciones (entre 0 y 100) hasta introducir un 0.
# Valida que las notas esten dentro del rango.

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Resumen de ventas usando compresion de listas y funciones' + '\033[0m')

notas = []
while True:
    try:
        nota = int(input('Introduzca nota (0 para detener): '))
        if nota == 0:
            break
        if nota < 0 or nota > 100:
            print('Nota invalida. Intente de nuevo.')
        else:
            notas.append(nota)
    except ValueError:
        print('Entrada invalida. Intente de nuevo.')

# Suma de notas
suma = sum(notas)
promedio = suma / len(notas)


print('--- Resultados ---')
print('Total de notas introducidas: ', len(notas))
print('Notas ingresadas:', notas)
print('Suma de notas: ', suma)
print(f'Promedio de notas: {promedio:.2f}')
print('Nota maxima: ', max(notas))
print('Nota minima: ', min(notas))
print(f'Notas menores al promedio ({promedio}): ', sum(1 for nota in notas if nota < promedio))
print('Lista de notas menores al promedio: ', [nota for nota in notas if nota < promedio])