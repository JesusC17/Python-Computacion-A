# p062-conversion-temperaturas.py
# Conversor de rango de temperatura ingresada en Celsius a Farenheit, de grado en grado

print('\033[2J\033[H', end='')
print('Conversor de rango de temperatura ingresada en Celsius a Farenheit, de grado en grado\n')

while True:
    ci = int(input('Introduce la temperatura inicial en °C: '))
    cf = int(input('Introduce la temperatura final en °C: '))
    print('-' * 50)
    while ci <= cf:
        f = (ci * 9/5) + 32
        print(f'{ci}°C = {f:.1f}°F')
        ci += 1

    if input('\nDeseas Continuar (S/N)?').upper() == 'N': break    
print('\nTerminamos...')
