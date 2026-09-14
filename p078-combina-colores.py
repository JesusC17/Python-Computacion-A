# p078-combina-colores.py
# Genera las posibles combinaciones de los colores o palabras

print('\033[2J\033[H', end='')
print('Genera las posibles combinaciones de los colores o palabras \n')

colores = input('Dame los colores separados por coma > ').replace(' ','').split(',')


for c1 in colores:
    for c2 in colores:
        if c1 != c2:
            print(f'{c1} - {c2}')
