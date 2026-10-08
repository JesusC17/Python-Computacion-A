# p112-datos-estudiante.py
# Gestion de datos de estudiante con un diccionario

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Gestion de datos de estudiante con un diccionario' + '\033[0m')

estudiante = {
    'nombre': 'Juan Perez',
    'edad': 20,
    'carrera':'Ingenieria en Sistemas',
    'email':'juan.perez1@uaz.edu.mx'
}

print(f'Datos del estudiante: {estudiante} = {len(estudiante)} elementos')

# Modificar un dato del estudainte
estudiante['edad'] = 21
estudiante['email'] = 'juan23@gmail.com'

print(f'Datos del estudainte: {estudiante} = {len(estudiante)} elementos')

# Agregar un nuevo dato
estudiante['promedio'] = 8.5
print(f'Datos del estudainte: {estudiante} = {len(estudiante)} elementos')

# mostrar las llaves del diccionario
print('Las llaves son: ')
for key in estudiante.keys():
    print(f' - {key}')

# Mostrar los valores del diccionario
print('Los valores son: ')
for value in estudiante.values():
    print(f' - {value}')

# Mostrar llaves y valores del dicconario
print('Las llaves y valroes son: ')
for key, value in estudiante.items():
    print(f' - {key}: {value}')