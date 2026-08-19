# p020-numero-suerte.py
# Programa que calcula numero de suerte basado en a;o de nacimiento

print("\033[2J\033[H", end="")
print('Programa que calcula numero de suerte basado en año de nacimiento\n')

año = int(input('Ingresa tu año de nacimiento: '))

millares = año // 1000
centenas = (año - (millares * 1000)) // 100
decenas = (año - (millares * 1000 + centenas * 100)) // 10
unidades = año - (millares * 1000 + centenas * 100 + decenas * 10)

print(f'"{millares}","{centenas}","{decenas}","{unidades}",')
numeroSuerte = millares + centenas + decenas + unidades

print(f'Tu numero de suerte es: {numeroSuerte}')