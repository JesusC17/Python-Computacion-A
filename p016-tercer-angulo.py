# p016-tercer-angulo.py
# programa que calcula el tercer angulo deun triangulo dando 2 angulos de un triángulo .

print("\033[2J\033[H", end="")
print('Programa que calcula el tercer angulo de un triangulo dando 2 angulos de un triángulo\n')

angulo1 = int(input('Ingresa el angulo 1: '))
angulo2 = int(input('Ingresa el angulo 2: '))

angulo3 = 180 - (angulo1 + angulo2)

print(f'El tercer angulo es de: {angulo3}')