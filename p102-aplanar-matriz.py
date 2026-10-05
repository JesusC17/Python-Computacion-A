# p102-aplanar-matriz.py
# Aplana una matriz de dos dimensiones a una lisa de 1 dimension usando compresion de listas

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Aplanar matriz a lista usando compresion de listas' + '\033[0m')

matriz = [[1, 2, 3], [-4, 5, 6], [-7, 8, 9]]

# Se aplana la matriz utilizando compresion de listas
aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [elemento for elemento in aplanada if elemento > 0]
negativos = [elemento for elemento in aplanada if elemento < 0]

print('Matriz original:', matriz)
print('Matriz aplanada:', aplanada)
print('Elementos positivos:', positivos)
print('Elementos negativos:', negativos)
