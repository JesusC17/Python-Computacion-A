# p126-procesar-diccionario.py

print('\033c', end='')

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina =  dict(zip(nombres, sueldos))

print('Diccionario de nomina: \n', nomina)

print('--- Iterando Llaves (keys) ---')
for nombre in nomina.keys():
    print(nombre)

print('--- Iterando Valores (values)---')
for valor in nomina.values():
    print(valor)

print('--- Iterando Llave y Valor (accediendo por llave) ---')
for nombre in nomina.keys():
    print(f'{nombre} -> {nomina[nombre]}')

print('--- Iterando Llave y Valor (items) ---')
for nombre, sueldo in nomina.items():
    print(f"'{nombre}', {sueldo:.2f})")

print('--- Calculos ---')
s = 0
for sueldo in nomina.values():
    s += sueldo
print(f'Suma total de sueldos: {s}')
p = s/len(nomina)
print(f'Promedio de sueldos: {p:.2f}')