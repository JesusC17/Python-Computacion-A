# p111-comprension-pares-cuadrados.py
# Genera una lista de 1 a n. Con compresion de listas crear una nueva lsita que 
# contenga los cuadrados unicamente de los numeros pares. Imprime la original, 
# la resultante de los cuadrados y la suma de los cuadrados

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Lista de 1 a n, se calculan los cuadrados de los pares y se suman' + '\033[0m')

n = int(input('Introduce el limite: '))

listaOr = list(range(1, n + 1))
listaCua = [numero ** 2 for numero in listaOr if numero % 2 == 0]


print('--- Resultados ---')
print(f'Lista original (1 a {n}): ', listaOr)
print('Cuadrados de numeros pares: ', listaCua)
print('Suma de los cuadrados: ', sum(listaCua))