# p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extras

print("\033[2J\033[H", end="")
print('Calcula la paga de un trabajador considerando horas extras\n')

print('Dame tus datos')
nombre = input('Nombre: ')
horas = int(input('Horas: '))
paga_hora = float(input('Paga x Hora: '))

horas_extra = paga_extra = 0

if horas > 40:
    paga_normal = 40 * paga_hora
    horas_extra = horas - 40
    paga_extra = horas_extra * (paga_hora * 2)

else:
    paga_normal = horas * paga_hora

total = paga_normal + paga_extra

print('Calculo de pagos ')
print(f'El trabajador {nombre} trabajo {horas} horas  a una paga de {paga_hora}')
print(f'Paga normal: {paga_normal}')
print(f'Horas extra: {horas_extra}')
print(f'Paga extra: {paga_extra}')
print(f'TOTAL: {total}')

print('\nFin del programa...')