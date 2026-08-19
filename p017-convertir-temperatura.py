# p017-convertir-temperatura.py
# Programa para convertir de grados Celsius a grados Farenheit

print("\033[2J\033[H", end="")
print('Programa para convertir de grados Celsius a grados Farenheit \n')

celsius = float(input('Ingresa los grados Celsius a convertir: '))

farenheit = (celsius * 9 / 5) + 32

print(f'La conversion de {celsius} °C corresponde a {farenheit} °F')