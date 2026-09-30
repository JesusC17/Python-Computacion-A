# p095-registro-estudiantes.py
"""""
Planteamiento del probelama: Registro de estudiantes para evento
Se esta organizando un evento y nececesitas registrar a los asistentes
El programa debe permitir al usuario introducir el nombre y la edad de cada persona
El registro termina cunadose itroduce un * como  nombre
Al finalizar, el sistema debe mostrar dos informes:
una lista de todos los asistentes que son mayores de edad (18 anios o mas)
y el nombre y la edad de la persona con mayoredad para entregarle un reconocimiento
"""""

print('\033[2J\033[H', end='')
nombres = []
edades = []

while True:
    nombre = input('Ingrese el nombre del asistente (o * para terminar): ')
    if nombre == '*':
        break
    try:
        edad = int(input('Ingrese la edad del asistente: '))
        nombres.append(nombre)
        edades.append(edad)
    except ValueError:
        print('Error: ingrese un número válido para la edad.')

if nombres:
    # Filtrar asistentes mayores de edad
    for i in range(len(edades)):
        if edades[i] >= 18:
            print(f'{nombres[i]} es mayor de edad con {edades[i]} años.')
    # Encontrar la persona con mayor edad
    max_edad = max(edades)
    indice_max = edades.index(max_edad)
    print(f'{nombres[indice_max]} es la persona con mayor edad con {edades[indice_max]} años.')