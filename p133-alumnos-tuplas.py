# p133-alumnos-tuplas.py
# Registro de alumnos usando una tupla de tuplas

# Creamos una tupla donde cada elemento es otra tupla con los datos
alumnos = (
    ('Ana', 'ISC', (9,10,9)),
    ('Luis', 'ITC', (8,9,10)),
    ('Luis', 'ISD', (10,8,9))
)

# Imprime el total de alumnos
print('Registro de alumnos:')
print('Total de alumnos: ', len(alumnos))

# Itera sobre la tupla y calcula el promedio
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f'{nombre} - {carrera} - {calificaciones} : {promedio:.2f}')

# Imprime los datos del primer alumno usando indices
primer_alumno = alumnos[0]
print('\nDatos del primer alumno:')
print('Nombre: ', primer_alumno[0])
print('Carrera: ', primer_alumno[1])
print('Calificaciones: ', primer_alumno[2])

# Crea la tupla de promedio usando compresion de tuplas
promedios = tuple(
    (nombre, sum(notas) / len(notas)) for nombre, _, notas in alumnos
)

print('\nPromedio de los alumnos: ', promedios)

# Crear tupla con los nombres de los alumnos
nombres = tuple(nombre for nombre, _, _, in alumnos)
print('\nNombres de los alumnos: ', nombres)