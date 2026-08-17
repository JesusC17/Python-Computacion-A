# -p005-calculadora-imc.py
# Calcular el IMC de una persona

print("\033[2J\033[H", end="")
print('Calculadora de indice de masa corporal IMC \n')

peso_kg = float(input('ingresa tu peso en kilogramos: '))
altura_m = float(input('ingresa tu altura en metros: '))

imc = peso_kg / (altura_m ** 2)

print(f'Si tu altura es {altura_m}m y tu peso es {peso_kg}kg tu IMC = {imc:.2f}')