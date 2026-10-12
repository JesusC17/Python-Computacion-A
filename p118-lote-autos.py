# p118-lote-autos.py
# Crear una lista de diccionarios para almacenar los datos de varios autos



autos = [
{"marca": "Toyota", "modelo": "Camry", "año": 2020, "precio": 25000},
{"marca": "Honda", "modelo": "Civic", "año": 2019, "precio": 22000},
{"marca": "Ford", "modelo": "Focus", "año": 2021, "precio": 23000}
]

autos.append({"marca": "Chevrolet", "modelo": "Malibu", "año": 2022, "precio": 27000})

print('\033c',end='')

print('Datos de los autos: ')
print(f'Todos los autos: {autos} - {len(autos)} elementos')
print('\nDatos de cada auto: ')
for auto in autos:
    print(auto)
    print()

# Mostrar los datos en forma de tabla
print('Datos de los autos en forma de tabla: ')
for k in autos[0].keys():
    print(f'{k:<10}', end=' | ')
print()
for auto in autos:
    for v in auto.values():
        print(f'{v:<10}', end=' | ')
    print()

# Mostrar los datos en forma de registros
print('\nDatos de los autos en forma de registro')
print('-'*60)
for auto in autos:
    for k, v in auto.items():
        print(f'{k:<12} : {v}')
print('')

