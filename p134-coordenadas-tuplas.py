# p134-coordenadas-tuplas.py
# 

print('\033c', end='')

zacatecas = ('Zacatecas', 22.77, -102.58)
guadalupe = ('Guadalaupe', 22.75, -102.52)

print('Tupla Zacatecas: ', zacatecas,', Tipo: ', type(zacatecas))
print('Tupla Guadalupe: ', guadalupe,', Tipo: ', type(guadalupe))


# Acceso a los elemetos d ela tupla usando indices
print('Acceso por indices (', zacatecas[0],'):')
print(f'\t Positivos -> Nombre: {zacatecas[0]}, Latitud: {zacatecas[1]}, Longitud: {zacatecas[2]}')
print(f'\t Negativos -> Nombre: {zacatecas[-3]}, Latitud: {zacatecas[-2]}, Longitud: {zacatecas[-1]}')

print('Acceso por indices (', guadalupe[0],'):')
print(f'\t Positivos -> Nombre: {guadalupe[0]}, Latitud: {guadalupe[1]}, Longitud: {guadalupe[2]}')
print(f'\t Negativos -> Nombre: {guadalupe[-3]}, Latitud: {guadalupe[-2]}, Longitud: {guadalupe[-1]}')

# Desempaquetar las tupals en variables para luego imprimirlas
nombre1, latitud1, longitud1 = zacatecas
nombre2, latitud2, longitud2 = guadalupe

print(f'{nombre1}: ({latitud1}, {longitud1})')
print(f'{nombre2}: ({latitud2}, {longitud2})')

# Reccorrer ubicaiones con ciclo for para mostrar informacion
for ciudad in [zacatecas, guadalupe]:
    print(f'Ubicacion: {ciudad[0]}, Coordenadas: ({ciudad[1]}, {ciudad[2]})')


# Calcular punto medio de las ubicaiones
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe

centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print(f'Punto medio aproximado: ', centro)

# Crear nuevla tupla para Zacatecas que incluya ZAC
nueva = zacatecas + ('ZAC',)
print('Nueva tupla Zacatecas: ', nueva)
print('Original sin cambios: ', zacatecas)

# Verificar si 'Zacatecas' pertenece a s tupla
print('"Zacatecas" pertenece a la tupla: ', 'Zacatecas' in zacatecas)
