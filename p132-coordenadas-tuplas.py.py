# p132-coordenadas-tuplas.py
# Registrp de coordenadas geograficas usando tuplas

zacatecas = ('Zacatecas', 22.7709, -102.5833)
guadalupe = ('Guadalaupe', 22.75, -102.52)

# Acceso a los elemetos d ela tupla usando indices
print('Coordenadas de Zacatecas:')
print('Tipo ', type(zacatecas))
print('Ciudad: ', zacatecas[0])
print('Latitud: ', zacatecas[1])
print('Longitud: ', zacatecas[2])

# Acceso a los elemetos d ela tupla usando desempaquetado
ciudad, latitud, longitud = guadalupe
print('\nCoordenadas de Guadalupe:')
print('Tipo: ', type(guadalupe))
print('Ciudad :', ciudad)
print('Latitud :', latitud)
print('Longitud :', longitud)

for lugar in [zacatecas, guadalupe]:
    print('\nCoordenadas de ', lugar[0])
    print('Latitud: ', lugar[1])
    print('longitud: ', lugar[2])


#Guion bajo para poder desempaquetar pero para no tomarlo en cuenta
_, lat1, lon1 = zacatecas           
_, lat2, lon2 = guadalupe

centro = ((lat1 + lat2) / 2, (lon1 + lon2) / 2)
print('Punto medio: ', centro)

#Verificar pertenencia
print('Zacatecas pertenece a la tupla: ', 'Zacatecas' in zacatecas)

# Crear otra tupla con datos extra
ampliada = zacatecas + ('Mexico',)

print('Tupla original: ', zacatecas)
print('Tupla ampliada: ', ampliada)