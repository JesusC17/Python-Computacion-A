# p128-municipios.py
# Gestion de un padron municipal usando conjuntos

municipios = {'Zacatecas', 'Guadalupe','Fresnillo','Jerez','Sombrerete','Fresnillo'}

print('\033c', end='')

print('Padron de municipios')
print('-'*30)
print('Municipios registrados:')
print(type(municipios))
for municipio in municipios:
    print(municipio)

#Consultar si un municipio esta registrado
print('Esta Zacatecas dentro de los municipios resgistrados? ','Zacatecas' in municipios)

# Altaas al padron de municipios
print('Agrefanod un municipio al padron')
municipios.add('Calera')
print(f'Municipio registrados: {municipios} - {len(municipios)}')

# Agregar varios municipios al padron
print('\nAgregando varios municipios al padron')
otros = {'Concepcion del Oro','Jalpa','Villanueva'}
municipios.update(otros)
print(f'Municipio registrados: {municipios} - {len(municipios)}')

# Eliminar un municipio del padorn con discard
print('\nELiminando un municipio del padron')
municipios.discard('Sombrerete')
print(f'Municipio registrados: {municipios} - {len(municipios)}')

# Eliminar un municipio del padorn con remove
print('\nELiminando un municipio del padron')
municipios.remove('Jerez')
print(f'Municipio registrados: {municipios} - {len(municipios)}')

# Eliminar un municipio del padorn con pop
print('\nELiminando un municipio del padron')
municipio_eliminado = municipios.pop()
print(f'Municipio eliminado: {municipio_eliminado}')
print(f'Municipio registrados: {municipios} - {len(municipios)}')


# Eliminando todo el conjunto
print('Eliminando el contenido del conjunto')
municipios.clear()
print(f'Municipio registrados: {municipios} - {len(municipios)}')
