# p029-calculadora-descuento.py
# Simula calculadora de descuentos basada en el monto de la compra

print("\033[2J\033[H", end="")
print('Simula calculadora de descuentos basada en el monto de la compra\n')

compra = float(input('Total de la compra? '))
descuento = porcentaje = 0

if compra > 2000:
    porcentaje = 0.20
elif compra > 1000:
    porcentaje = 0.10
elif compra > 500:
    porcentaje = 0.05

descuento = compra * porcentaje
total = compra - descuento

print('Resumen de la compra')
print(f'Total de la compra      : {compra:,.2f}')
print(f'Porcentaje descuento    : {porcentaje*100}%')
print(f'Descuento               : {descuento:,.2f}')
print(f'Total a pagar               : {total:,.2f}')