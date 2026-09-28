# p091-lista-de-gastos_b.py
# Control de gastos mensuales

gastos = []

while True:
    print('\n--- Control de gastos ---')
    print('1. Ver gastos')
    print('2. Agregar gasto')
    print('3. Modificar gasto')
    print('4. Eliminar gasto')
    print('5. Ver total')
    print('6. Salir')

    opcion = input('Seleccione una opción: ').strip()

    if opcion == '1':
        if gastos:
            print('\nGastos actuales:')
            for indice, gasto in enumerate(gastos, start=1):
                print(f'{indice}. ${gasto:.2f}')
            print('Éxito: gastos mostrados.')
        else:
            print('No hay gastos registrados.')

    elif opcion == '2':
        try:
            gasto = float(input('Ingrese el monto del gasto: '))
            gastos.append(gasto)
            print(f'Éxito: gasto de ${gasto:.2f} agregado.')
        except ValueError:
            print('Error: ingrese un monto numérico.')

    elif opcion == '3':
        try:
            indice = int(input('Ingrese el número del gasto a modificar: ')) - 1
            if 0 <= indice < len(gastos):
                nuevo_gasto = float(input('Ingrese el nuevo monto: '))
                anterior = gastos[indice]
                gastos[indice] = nuevo_gasto
                print(
                    f'Éxito: gasto de ${anterior:.2f} '
                    f'modificado a ${nuevo_gasto:.2f}.'
                )
            else:
                print('Error: gasto no encontrado.')
        except ValueError:
            print('Error: ingrese un número válido.')

    elif opcion == '4':
        try:
            indice = int(input('Ingrese el número del gasto a eliminar: ')) - 1
            if 0 <= indice < len(gastos):
                eliminado = gastos.pop(indice)
                print(f'Éxito: gasto de ${eliminado:.2f} eliminado.')
            else:
                print('Error: gasto no encontrado.')
        except ValueError:
            print('Error: ingrese un número entero válido.')

    elif opcion == '5':
        total = sum(gastos)
        print(f'Total de gastos: ${total:.2f}')
        print('Éxito: total calculado.')

    elif opcion == '6':
        print('Saliendo de la aplicación.')
        break

    else:
        print('Error: opción inválida. Seleccione un número del 1 al 6.')

