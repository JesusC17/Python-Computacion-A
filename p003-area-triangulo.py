# p003-area-triangulo.py
# Calcular el area de un triangulo

print("\033[2J\033[H", end="")

print('Calculando el area de un triangulo \n')

print('Dame la base y la altura del triangula separadas por <Enter>')
base, altura = int(input()), int(input())

area = (base * altura) / 2

print(f'El triangulo de base {base} y altura {altura}, tiene un area de {area:.2f}')