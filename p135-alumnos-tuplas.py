# p135-alumnos-tuplas.py 
# Registro de alumnos mediante tupla de tuplas


print('\033c', end='')

alumnos = (
    ('Ana', 'ISC', (9, 10, 9, 8)),
    ('Luis', 'ISW', (8, 8, 9, 10)),
    ('Mar', 'ISC', (10, 9, 10, 10))
)

print('Registro de los alumnos: ', alumnos)
print('Total de alumnos: ', len(alumnos))

# Recorrer los registros emdiante desempaquetado

for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f'Nombre: {nombre}, Carrera: {carrera}, Promedio:{promedio:.2f}')

# Nueva tupla con nombres y promedios
alumnos_promedios = tuple(
    (nombre, sum(calificaciones) / len(calificaciones))
    for nombre, carrera, calificaciones in alumnos
)

print('\nPares (nombre, promedio):', alumnos_promedios)

# Encontrar el alumno con el mejor promedio
mayorPromedio = 0
mejorAlumno = ''
for nombre, promedio in alumnos_promedios:
    if promedio > mayorPromedio:
        mayorPromedio = promedio
        mejorAlumno = nombre

print(f'Alumno con mejor promedio: {mejorAlumno} con {mayorPromedio}')

# Consultar calificaiones usando indices de tuplas anidadas. Para cada alumno
# mostrar cuantas veces aparece 10 con count() y la posicion de la primera calificacion
# con index()

for nombre, _, calificaciones in alumnos:
    print(f'{nombre} -> Conteo de los 10s: {calificaciones.count(10)}, Indice de la primera calificacion: {calificaciones.index(10)}')

# Ordenar los pares (nombre, promedio) por pormedio de menor a mayor usando sorted() sin usar lambday mostrar resultado como tupla
alumnos_ordenados = list(alumnos_promedios)

for i in range(len(alumnos_ordenados)):
    for j in range(i + 1, len(alumnos_ordenados)):
        if alumnos_ordenados[i][1] > alumnos_ordenados[j][1]:
            alumnos_ordenados[i], alumnos_ordenados[j] = alumnos_ordenados[j], alumnos_ordenados[i]

alumnos_ordenados = tuple(alumnos_ordenados)

print('\nOrdenados por promedio:', alumnos_ordenados)

# Formar y mostrar nueva tupla con nombre "Eva", carrera "ISC" y
# califiocaciones (9, 9, 10) sin modificar la origianl
nueva = alumnos + (('Eva', 'ISC', (9, 9, 10)),)
print('Tupla original intacta: ', alumnos)
print('Nueva tupla con Eva: ', nueva)