# p113-calificaciones-estudiante.py
# Procesa calificaciones de un estudiante ocn un diccionatio

print('\033[2J\033[H', end='')

materias = ['Matematicas','Fisica','Quimica','Historia','Lengua', 'Ingles']
calificaciones = [8.5, 9.0, 7.5, 6.0, 8.0, 9.5]

calificaciones_estudiante = dict(zip(materias, calificaciones))
print(f'Calificaciones del estudiante: {calificaciones_estudiante} = {len(calificaciones_estudiante)} elementos')

# Agregar dos nuevas calificaiones
calificaciones_estudiante['Educacion Fisica'] = 10.0
calificaciones_estudiante['Arte'] = 9.0
print(f'Calificaciones del estudiante: {calificaciones_estudiante} = {len(calificaciones_estudiante)} elementos')

# Actualizar 3 calificaciones del estudiante
calificaciones_estudiante['Matematicas'] = 9.0
calificaciones_estudiante['Fisica'] = 8.5
calificaciones_estudiante['Historia'] = 7.0
print(f'Calificaciones del estudiante: {calificaciones_estudiante} = {len(calificaciones_estudiante)} elementos')

# Eliminar 2 calificaciones del estudiante usando pop
calificaciones_estudiante.pop('Quimica')
calificaciones_estudiante.pop('Lengua')
print(f'Calificaciones del estudiante: {calificaciones_estudiante} = {len(calificaciones_estudiante)} elementos')


# Mostrar el par llave-valor de las calidicaciones del estudiante, y promedio de calificaciones
print('Las llaves y valores son: ')
total = 0
for materia, calificacion in calificaciones_estudiante.items():
    print(f' -{materia}: {calificacion}')
    total += calificacion
promedio = total / len(calificaciones_estudiante)
print(f'Promedio de calificaciones: {promedio:.2f}')
