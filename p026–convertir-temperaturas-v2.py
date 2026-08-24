# p026–convertir-temperaturas-v2.py
# Convierte temperaturas de celcius a farenheit y viceversa

print("\033[2J\033[H", end="")
print('Convierte temperaturas de celcius a farenheit y viceversa\n')

print('[1] Convertir de Frenheit a Celsius')
print('[2] Convertir de Celsius a Frenheit')

op = int(input('Elige ? '))

if op == 1:
    print('\nConvirtiendo de Farenheit a Celsius')
    f = float(input('Ingresa la teperatura en grados Farenheit: '))
    c = ( f - 32 ) * 5 / 9
    print(f'{f} grados Farenheit, equivalen a {c} grados Celsius' )
    
else:
    if op == 2:
        print('\nConvirtiendo de Celsius a Farenheit')
        c = float(input('Ingresa la teperatura en grados Farenheit: '))
        f = ( c * 9 / 5 ) + 32
        print(f'{c} grados Celsius, equivalen a {f} grados Farenheit')

    else:
        print('\nOpcion INVALIDA')

print('\nFin del programa...')