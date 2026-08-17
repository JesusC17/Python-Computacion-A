# p006-conversor-temperatura.py
# Convertir temperatura dade en grados celsius a Farenheit

print("\033[2J\033[H", end="")
print('Convertir temperatura dade en grados celsius a Farenheit \n')

#f = ( float(input('Grados Celcius: ')) * 9 / 5.0) + 32

c = float(input('Grados Celcius: '))
f = (c * 9 / 5) + 32

print(f'La temperatura de {c} grados centigrados equivale a {f} grados Farenheit')