# p116-conversion-divisas.py
# Implementar un conversor de divisas a pesos mexicanos
# Definir un diccionaroi de conversoines con las tasas de
# cambio USD, EUR, GBP, JPY, CAD a MXN

print('\033c',end='')

conversiones = {
    'USD': 18.50,
    'EUR': 20.00,
    'GBP': 23.00,
    'JPY': 0.14,
    'CAD': 14.00
}

# Mostrar opciones de divisas a convertir

print('Opciones de divisas: ')
for divisa in conversiones:
    print(f' - {divisa}')

# Solicitar al usuario la cantida d a convertir
cantidad = float(input('Ingresa la cantidad a converit: '))
while True:
    divisa_origen = input('Ingrese la divisa de origen').upper()
    if divisa_origen in conversiones:
        break
    print('Divisa de origen no valida. Intente nuevamente')

pesos_mxn = cantidad * conversiones[divisa_origen]
print('Resultado de la conversion: ')
print(f'{cantidad} {divisa_origen} son {pesos_mxn:.2f} pesos mexicanos (MXN).')