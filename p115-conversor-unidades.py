# p115-conversor-unidades.py
# Crear un conversor de unidades de longitud
# Definir un diccionario conversiones que almacene los
# factores para converti 'km', 'm', 'cm' y 'mm' a metros

print('\033c',end='')

conversiones = {
    'km': 1000.0,
    'm': 1.0,
    'cm': 0.01,
    'mm':0.001
}

cantidad = float(input('Ingrese la cantidad a convertir: '))

while True:
    unidad_origen = input('Ingrese la unidad de origen (km, m, cm, mm): ').lower()
    if unidad_origen in conversiones:
        break
    print('Unida de origen no valida. Intente nuevamente')

metros = cantidad * conversiones[unidad_origen]
print('Resultado de la conversion: ')
print(f'{cantidad} {unidad_origen} son {metros:.4f} metros')