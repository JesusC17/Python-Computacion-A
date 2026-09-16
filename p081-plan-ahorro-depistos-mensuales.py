# p081-plan-ahorro-depistos-mensuales.py
# Programa que simula un plan de ahorro

print('\033[2J\033[H', end='')
print('Programa que simula un plan de ahorro \n')

saldo_i = float(input('Monto inicial de ahorro: '))
deposito_m = float(input('Deposito mensual: '))
interes_m = float(input('Tasa de interes mensual (%): '))
meses = int(input('Numeor de meses a simular: '))


print('\n--- Plan de Ahorro Detallado ---')
saldo_f = interes = 0

for i in range(1, meses+1):
    saldo_f = (saldo_i * (1 + interes_m/100)) + 100
    interes = saldo_i * (interes_m / 100)
    print(f'Mes {i}: Saldo Inicial: ${saldo_i:.2f} \t| Interes: ${interes:.2f} \t| Saldo Final: ${saldo_f:.2f}')
    saldo_i = saldo_f

print(f'\nAl final de {meses} meses. tendras ${saldo_f:.2f}')
