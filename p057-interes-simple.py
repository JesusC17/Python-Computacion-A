# p057-interes-simple.py
# Calcula los años necesarios para alcanzar una mea de ahorro

print('\033[2J\033[H', end='')
print('Calcula los años necesarios para alcanzar una mea de ahorro\n')

ci = float(input('Capital inicial: '))
ti = float(input('Tasa de interes anual (%):'))
ma = float(input('Meta ahorro: '))

ca = ci
anios = iaf = 0
td = ti / 100

while ca <= ma:
    print(f'{anios} - {ca:>,.2f}')
    iaf = ca * td
    ca += iaf 
    anios += 1

print(f'Para llegar a {ma} deben pasar {anios} años, el capital es {ca}')