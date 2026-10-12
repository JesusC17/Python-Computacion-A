# p120-reporte-ventas.py
# Crear una lista de diccionarops para representar un reporte de ventas de una tineda
# Cada compra registra > nombre del cliente, producto, cantidad y precio
# Cada compra debe ser un diccionario almacenado en una lista de compras

compras = []

# borrar pantalla de la consola
print('\033c',end='')

print('\n Registro de compras de la tienda  \n')
n = int(input('Ingrese el numero de compras que desea realizar: '))
for i in range(1, n+1):
    print(f'\n Compra {i}:')
    compra = {
        'cliente': input('Nombre: '),
        'producto': input('Producto: '),
        'cantidad': int(input('Cantidad: ')),
        'precio': float(input('Precio: '))
    }
    compras.append(compra)

# Mostrar los datos de cada compra en la lista
print(f'\nTodas las compras: {compras} - {len(compras)} elementos')

# Consolidar las compras por cliente
# al final quiero saber el total de productos y dinero gastado
clientes = {}
for compra in compras:
    cliente = compra['cliente']
    if cliente not in clientes:
        clientes[cliente] = {'total_productos': 0, 'total_gastado': 0.0}
    clientes[cliente]['total_productos'] += compra['cantidad']
    clientes[cliente]['total_gastado'] += compra['cantidad'] * compra['precio']

# Mostrar el reporte consolidado
print('\nReporte consolidado por cliente: ')
for cliente, datos in clientes.items():
    print(f'Cliente: {cliente}')
    print(f' Total de productos comprados: {datos['total_productos']}')
    print(f' Total gastado: ${datos['total_gastado']:.2f}\n')

print('Diccionario de clientes con totales: ')
print(clientes)