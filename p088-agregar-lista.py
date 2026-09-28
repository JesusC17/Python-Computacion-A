# p088-agregar-lista.py
# Agregar elementos de una lista

# Borrar pantalla
print('\033[2J\033[H', end='')
print('Agregar elementos de una lista \n')

nums = [10, 20, 30, 40, 60, 70, 10, 20, 99]

print('\nLongitud y contenido de la lista de numeros: ')
print(f'Contenido: {nums} | Longitud: {len(nums)}')

print('\nAgregar 90 y 100 al final de la lista')
nums.append(90)
nums.append(100)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nInsertar 80 en la posicion 4')
nums.insert(4, 80)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nExtender la lista con [110, 120, 130]')
nums.extend([110, 120, 130])
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

