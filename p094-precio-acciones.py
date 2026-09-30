# p094-precio-acciones.py
# Analisi de precios de acciones diarias
# Dada una lsita de precios de cieere de ua accion durante la semana,
# Encontrar el precio mas alto, el mas bajo y el dia en que ocurrieron

print('\033[2J\033[H', end='')
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
precios = [150.25, 152.30, 149.80, 151.00, 153.45, 154.10, 155.00]

precio_mas_alto = max(precios)
precio_mas_bajo = min(precios)
idice_mas_alto = precios.index(precio_mas_alto)
idice_mas_bajo = precios.index(precio_mas_bajo)

print('Analisis de preciso de acciones: ')
print(f'Precio mas alto: {precio_mas_alto} el dia {dias[idice_mas_alto]}')
print(f'Precio mas bajo: {precio_mas_bajo} el dia {dias[idice_mas_bajo]}')

