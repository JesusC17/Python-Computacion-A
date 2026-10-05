# p103-resumen-ventas.py
# Trandforma y filtra ventas con compresion de listas

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Resumen de ventas usando compresion de listas' + '\033[0m')

ventas = [1000, 2000, 3000, 400, 500]# ventas del mes

# ventas mayores a 1000 aplica 10% de descuento, menores a 1000  aplica un 5% de descuento
ventas_descuento = [v * 0.9 if v >= 1000 else v * 0.95 for v in ventas]

# saques ventas relevantes si son mayores a 100
ventas_relevantes = [v for v in ventas_descuento if v > 100]

print('Ventas originales:', ventas)
print('Ventas con descuento:', ventas_descuento)
print('Ventas relevantes (mayores a 1000):', ventas_relevantes)