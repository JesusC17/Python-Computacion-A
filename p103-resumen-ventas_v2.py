# p103-resumen-ventas_v2.py
# Transforma una lista de ventas usando una funcion y compresion de lsitas
# La transformacion aplica 3 pasos en una misma funcion:
# La funcion procesa la transformacion, luego en el programa principal es llamada

# esta funcion aplica 3 transformaciones a cada elemento que le llega como parametro (una venta)
# regresa el resultado de la transformacion

def transformar_venta(venta):
    # paso 1: si la venta es mayor o iguala a 1000 aplica un descuento del 10%
    if venta >= 1000:
        venta *= 0.9
    else:
        # paso 2: si la venta es menor a 1000 aplica un descuento del 5%
        venta *= 0.95

    return venta

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Resumen de ventas usando compresion de listas y funciones' + '\033[0m')

# ventas del mes (10) varias con decimales
ventas = [1000, 2000, 3000, 400, 500, 1500.50, 2500.75, 800.25, 1200.10, 600.60, 2500.80]
ventast = [transformar_venta(v) for v in ventas]

print('Ventas originales:', ventas)
print('Ventas transformadas:', ventast)
