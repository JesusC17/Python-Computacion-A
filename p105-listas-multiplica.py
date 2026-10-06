# p105-listas-multiplica.py
# Lee dos listas de 5 elementos numericos cada una. Se crea una tercera lista
# multiplicando los elementos de las dos listas

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Multiplicacion de listas' + '\033[0m')

lista_a = []
lista_b = []

print('Introduza 5 numeros para la Lista A: ')
for i in range(5):
    num = int(input(f'Numero {i + 1}: '))
    lista_a.append(num)

print('Introduza 5 numeros para la Lista B: ')
for i in range(5):
    num = int(input(f'Numero {i + 1}: '))
    lista_b.append(num)

lista_c = [a * b for a, b in zip(lista_a, lista_b)]

print('--- Resultados ---')
print('Lista A: ', lista_a)
print('Lista B: ', lista_b)
print('Lista C (A * B): ', lista_c)