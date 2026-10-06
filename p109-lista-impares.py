# p109-lista-impares.py
# Leer un entero n. Llena una lista con los primeros n numeros impares

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Crea una lista con los primeros n numeros impares solicitados por usuario' + '\033[0m')

numeros = []
div3 = []

n = int(input('Introduzca la cantidad de numeros impares (n): '))
i = 1
while True:
    if i % 2 != 0:
        numeros.append(i)
    if i % 3 == 0:
        div3.append(i)
    if len(numeros) == n:
        break
    i += 1

suma = sum(numeros)
promedio = suma / len(numeros)

print('--- Generacion de Lista ---')
print(f'Lista de los primeros {n} numeros impares: {numeros}')

print('--- Calculos ---')
print('Suma de los numeros: ', suma)
print(f'Promedio de los numeros: {promedio:.2f}')

print('--- Divisibles entre 3 ---')
print('Numeros divisibles entre 3: ', div3)
print('Suma de los numeros divisibles entre 3: ', sum(div3))

print('--- Busqueda ---')

num = int(input('Introduzca el elemento a buscar: '))
if num in numeros:
    posicion = numeros.index(num) 
    print(f'El elemento {num} esta en la lista en la posicion (indice) {posicion}')
else:
    print('El elemento no pertenece a la lista')