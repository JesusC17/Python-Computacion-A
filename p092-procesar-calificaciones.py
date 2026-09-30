# p092-procesar-calificaciones.py
# Porcesa n calificaciones entre 1 y 10 en una lista hasta introducir 999
# Al final muestra: la lista, la suma, promedio, la mas alta, la mas baja,
# cuantos alumnos mayores al promedio
# valida que no introduzca letra en lugar de numeros


calificaciones = []
suma = 0
# borrar la consola
print('\033[2J\033[H', end='')

while True:
    try:
        calificacion = float(input('Ingrese una calificación entre 1 y 10 (o 999 para terminar): '))
        if calificacion == 999:
            break
        elif 1 <= calificacion <= 10:
            calificaciones.append(calificacion)
            suma += calificacion
        else:
            print('Error: la calificación debe estar entre 1 y 10.')
    except ValueError:
        print('Error: ingrese un número válido.')

if calificaciones:
    promedio = suma / len(calificaciones)
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)
    alumnos_mayores_promedio = sum(1 for cal in calificaciones if cal > promedio)   #Cuenta los alumnos mayores al promedio
                            # Suma de 1 en uno en caso de cumplir la condicion, recorre posicoines con for
    print('\nResultados:')
    print(f'Calificaciones ingresadas: {calificaciones}')
    print(f'Suma de calificaciones: {suma}')
    print(f'Promedio de calificaciones: {promedio:.2f}')
    print(f'Calificación más alta: {calificacion_maxima}')
    print(f'Calificación más baja: {calificacion_minima}')
    print(f'Alumnos con calificación mayor al promedio: {alumnos_mayores_promedio}')



