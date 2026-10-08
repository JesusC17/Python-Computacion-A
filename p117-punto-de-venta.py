# p117-punto-de-venta.py
# Crear un sistema simlpe de punto de venta (POS) para un puesto de comida

comida = {
    'Hamburgues': 5.0,
    'Papas Fritas': 2.5,
    'Rfresco': 1.5,
    'Hot Dog': 3.0,
    'Pizza': 8.0
}

print('\033c',end='')
print('Menu de productos:')
for producto, precio in comida.items():
    print(f'- {producto}: ${precio:.2f}')

#Tomar orden: Preguntar al usuario que desea ordena ren un buvle
# Si el producto no esta en el menu, informele
# Si el producto existe, solicitar la cantida

orden = {}
while True:
    producto = input('Ingrese el producto que desea ordenar (presiona <Enter> para finalizar): ')
    if producto == '':
        break
    if producto not in comida:
        print('Producto no disponible. Intente nuevamente')
        continue
    cantidad = int(input(f'Ingrese la cantidad de {producto}: '))
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad

print('\n Recibo de compra: ')
total_general = 0
for producto, cantidad in orden.items():
    subtotal = comida[producto] * cantidad
    total_general += subtotal
    print(f'- {producto} x {cantidad}: ${subtotal:.2f} ')
print(f'Total generado: {total_general:.2f}')
