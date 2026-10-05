# p098-cuadrados-lista.py
# Genera cuadrados usando compresion de listas

print('\033[2J\033[H', end='')
print('Cuadrados de 1 a n usando compresion de listas')
n = int(input('Ingrese el valor de n:'))

numeros = list(range(1, n + 1))
cuadrados = [x ** 2 for x in numeros]  # Compresion de lista para calcular el cuadrado

print('Los numeros del 1 al', n, 'son:', numeros)
print('Los cuadrados del 1 al', n, 'son:', cuadrados)
