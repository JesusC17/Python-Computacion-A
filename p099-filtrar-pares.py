# p099-filtrar-pares.py
# Filtra los numeros pares de una listra de numeros introducidos usando compresion de listas

print('\033[2J\033[H', end='')
print('Filtrar numeros pares de una lista usando compresion')

cant = int(input('Ingresa la cantidad de numeros a introducir: '))
numeros = []

#se introducen los numeros en la lista
for i in range(cant):
    num = int(input(f'Ingresa el numero {i + 1}: '))
    numeros.append(num)

# Se filtran los numeros pares e impares usando la compresion de listas
pares = [x for x in numeros if x % 2 == 0] # par
impares = [x for x in numeros if x % 2 != 0] # impar

print('Los numeros introducidos son:', numeros)
print(f'Los numeros pares son: {pares} - Cantidad: {len(pares)}')
print(f'Los numeros impares son: {impares} - Cantidad: {len(impares)}')
