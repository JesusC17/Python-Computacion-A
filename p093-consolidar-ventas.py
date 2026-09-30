# p093-consolidar-ventas.py
# Una empresa tiene 2 sucursales y desdea consolidar las ventas de cada una de ellas en una sola lista.
# Se ingresan n ventas para cada sucursal el usuario lo define

ventas1 = []
ventas2 = []

print('\033[2J\033[H', end='') 
n = int(input('Ingrese el numero de ventas: '))

# Ingresar ventas para la primera sucursal
print('\nIngrese las ventas para la primera sucursal: ')
for i in range(n):
    while True:
        try:
            venta = float(input(f'Venta {i + 1}: '))
            ventas1.append(venta)
            break
        except ValueError:
            print('Error: ingrese un número válido.')

# Ingresar ventas para la segunda sucursal
print('\nIngrese las ventas para la segunda sucursal: ')
for i in range(n):
    while True:
        try:
            venta = float(input(f'Venta {i + 1}: '))
            ventas2.append(venta)
            break
        except ValueError:
            print('Error: ingrese un número válido.')

# Consolidar las ventas en una sola lista
ventas_consolidadas = ventas1 + ventas2
print('\nVentas consolidadas: ')
for i, venta in enumerate(ventas_consolidadas, start=1):
    print(f'Venta {i}: {venta}')

# Total de ventas en dinero
total_ventas = sum(ventas_consolidadas)
print(f'\nTotal de ventas: {total_ventas}')