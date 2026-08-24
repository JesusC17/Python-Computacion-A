# p028-retira-cuenta.py
# Simula el retiro de dinero de una cuenta

print("\033[2J\033[H", end="")
print('Simula el retiro de dinero de una cuenta con validacion\n')

saldo_cuenta = 1500.00

cantidad_retiro = float(input(f'Cantidad a retirar de la ceunta {saldo_cuenta}? '))

if cantidad_retiro > 0:
    print('Procedemmos al retiro... ')
    if cantidad_retiro <= saldo_cuenta:
        nuevo_saldo = saldo_cuenta - cantidad_retiro
        print(f'\nRetiro exitoso, tu nuevo saldo es {nuevo_saldo}')
    else:
        print(f'Quieres retirar {cantidad_retiro} pero tienes {saldo_cuenta} NO TE ALCANZA')
else:
    print('\nLa cantidad a retirar debe ser un numero positivo')


print('Gracias por usar nuestro servicio')
