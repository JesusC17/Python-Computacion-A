# p124-agregar-diccionario.py

ventas = {'Juan': 1550, 'Jose': 2600, 'Maria': 2220}

print('\033c',end='')
print('Ventas iniciales:\n', ventas)

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567

ventas.update({'Andrea': 9567, 'Miguel': 1234})

print('Ventas actualizadas:\n', ventas)