# p035-tipo-triangulo.py
# Clasificar un triangulo segun la longitud de sus lados

print('\033[2J\033[H', end='')
print('Clasificar un triangulo segun la longitud de sus lados')

lado_a = float(input('Longitud del lado A: '))
lado_b = float(input('Longitud del lado B: '))
lado_c = float(input('Longitud del lado C: '))

if lado_a == lado_b and lado_b == lado_c:
    print(f'\n Es un triangulo EQUILATERO, todos sus lados son iguales')
elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
    print(f'\n Es un triangulo ISOCELES, al menos dos lados son iguales')
else:
    print(f'\n Es un triangulo ESCALENO, todos sus lados son diferentes')

print('\nProceso terminado')
    
