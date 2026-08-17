# -p004-paga-trabajador.py
# Calcular la paga d eun trabajador

print("\033[2J\033[H", end="")
print('Calculando la paga de un trabajado \n')

# Entrada
nombre = input('Dame tu nombre? ')
horas = int(input('Horas ?'))
paga = float(input('Paga ?'))

# Proceso
tasa = 0.03
pagaBruta = horas * paga
impuesto = pagaBruta * tasa
pagaNeta = pagaBruta - impuesto

# Salida
print('Resumen de pagos \n')
print(f'El trabajador {nombre}, trabajo {horas}, a una paga de {paga}')
print(f'Paga Bruta : {pagaBruta:>10,.2f}')
print(f'Impuesto : {impuesto:>10,.2f}')
print(f'Paga Neta : {pagaNeta:>10,.2f}')