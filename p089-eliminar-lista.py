# p089-eliminar-lista.py
# Eliminar elementos de una lista

# Borrar pantalla
print('\033[2J\033[H', end='')
print('\nEliminar elemntos de una lista ')

nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print('\nLongitud y contenido de la lista de numeros: ')
print(f'Contenido: {nums} | Longitud: {len(nums)}')

print('\nEliminar el 15 de la lista')
nums.remove(15)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nEliminar el elemneto en la posicion 3')
del nums[3]
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nEliminar el elemtno en posicion 5 usando pop()')
num =nums.pop(5)
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')
print(f'\nElemento eliminado: {num}')

print('\nEliminar el ultimo elemedo usando pop() sin parametros')
num = nums.pop()
print(f'Elemento eliminado: {num} | Contenido actualizado: {nums} | Longitud: {len(nums)}')

print('\nEliminar todos los elementos de la lista usando clear()')
nums.clear()
print(f'Contenido actualizado: {nums} | Longitud: {len(nums)}')