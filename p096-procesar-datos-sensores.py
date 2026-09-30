# p096-procesar-datos-sensores.py
# Planteamiento del problema: Procesamiento de datos de sensores
#Se tienen dos sensores que recogen 10 mediciones numéricas cada uno.
# Necesitamos un programa que realice las siguientes tareas:

from random import randint
print('\033[2J\033[H', end='')

sensor1 = []
sensor2 = []

# Genere dos listas con 10 números aleatorios (entre 1 y 10) para simular los
# datos de cada sensor y las muestre.
mediciones = 10
for _ in range(mediciones):
    sensor1.append(randint(1, 10))
    sensor2.append(randint(1, 10))
print('Datos del sensor 1:', sensor1)
print('Datos del sensor 2:', sensor2)

# Aplique una "transformación" a los datos, que consiste en elevar al cuadrado
# cada medición en ambas listas.
for i in range(mediciones):
    sensor1[i] = sensor1[i] ** 2
    sensor2[i] = sensor2[i] ** 2
print('\nDatos del sensor 1 después de la transformación:', sensor1)
print('Datos del sensor 2 después de la transformación:', sensor2)

# Cree una tercera lista que contenga la suma combinada de los datos
# transformados de ambos sensores (la suma del primer elemento de la lista 1 con
# el primero de la lista 2, y así sucesivamente).

total_suma =[]
for i in range(mediciones):
    total_suma.append(sensor1[i] + sensor2[i])
print('\nSuma combinada de los datos transformados de ambos sensores:', total_suma)
