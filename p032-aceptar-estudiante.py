# p032-aceptar-estudiante.py
# Aceptar estdiantes en base a edad y calificaciones (usando OR)
# Condiciones edad >= 18 y  c1 y c1 >= 8

print("\033[2J\033[H", end="")
print('Aceptar estdiantes en base a edad y calificaciones (usando OR)')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))

if edad < 18:
    print(f'\n{nombre}, no aceptamos menores de edad')
else:
    print(f'\n{nombre}, continuamos con el proceso')
    print('Dame tus dos calificaciones separadas por espacio: ')
    c1, c2 = map(float, input().split())
    if c1 < 8 or c2 < 8:
        print(f'\n{nombre}, no aceptamos calificaciones menores a 8...')
    else:
        print(f'{nombre} bienvenido a la Universidad')

print('Proceso terminado')