# p080-compara-rendimiento-inversion.py
# Programa que compara el rendimiento de dos fondos de inversion a lo largo de varios a;os

print('\033[2J\033[H', end='')
print('Programa que compara el rendimiento de dos fondos de inversion a lo largo de varios años \n')

print('--- Fondo de Inversion A ---')
mont_a = float(input('Monto inicial: '))
ti_a = float(input('Tasa de interes anual (%): '))

print('--- Fondo de Inversion B ---')
mont_b = float(input('Monto inicial: '))
ti_b = float(input('Tasa de interes anual (%): '))

anios = int(input('\nAños a proyectar: '))


print('\n--- Comparacion de Rendimientos Anuales ---')
print('Año     |      Fondo A  |       Fondo B     ')
print('-'*43)

for i in range(1, anios + 1):
    mont_a *= (1 + ti_a/100 ) 
    mont_b *= (1 + ti_b/100 ) 
    print(f'{i}\t|$\t{mont_a:.2f}\t|$\t{mont_b:.2f}\t')

if mont_a > mont_b:
    print(f'\nResultado final: El fondo A (${mont_a:.2f}) supero al Fondo B (${mont_b:.2f})')
else:
    print(f'\nResultado final: El fondo B (${mont_b:.2f}) supero al Fondo A (${mont_a:.2f})')
