# p119-registro-estudiantes.py
# Crear una lista de diccionarios para almacenar los datos de varios estudiantes
# nombre, edad, carrera y promedio

estudiantes = [
    {'nombre': 'Juan Peres', 'edad': '20', 'carrera':'Ingenieria de Sistemas', 'promedio': 8.5},
    {'nombre': 'Maria Lopez', 'edad': '22', 'carrera':'Medicina', 'promedio': 9.2},
    {'nombre': 'Pedro Lopes', 'edad': '21', 'carrera':'Arquitectura', 'promedio': 8.9}
]

print('\033c',end='')
#Mostrar los datos de cada destidainte en la lista
print(f'\nTodos los estudiantes: {estudiantes} - {len(estudiantes)} elementos')



while True:
    nombre = input('Ingrese el nombre del estudiante (o preisone Enter para salir): ')
    if nombre == '':
        break
    edad = int(input('Ingrese la edad del estudiante: '))
    carrera = input('Ingrese la carrera del estudiante: ')
    promedio = float(input('Ingrese el promedio del estudiante: '))
    estudiantes.append({'nombre': nombre, 'edad': edad, 'carrera': carrera, 'promedio': promedio})
    print(f'Estudiante {nombre} agregado correctamente.')

print(f'\nTodos ;ps estudiantes: {estudiantes} - {len(estudiantes)} elementos')

#Mostrar los datos en forma de tabla
print('\n Datos en formato de Tabla:')
print('-'*60)
for k in estudiantes[0].keys():
    print(f'{k:<13}', end='')
print('')
for alumno in estudiantes:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print('')

print('\n Datos en forma de Registro y Calculo de Promedios: ')
print('-'*60)
s = 0
for est in estudiantes:
    s += est['promedio']
    for k, v in est.items():
        print(f'{k:<10} : {v}')
    print('')

print('\nCalculo de Promedios: ')
print('-'*60)
p = s / len(estudiantes)
print(f'La suma es {s}')
print(f'El promedio es {p:.2f}')