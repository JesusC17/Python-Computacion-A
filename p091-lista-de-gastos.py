# Aplicación para almacenar y manipular gastos mediante un menú.

gastos = []


def mostrar_menu():
    print('\033[2J\033[H', end='')
    print('Aplicación de gastos')
    print('1. Agregar gasto')
    print('2. Mostrar gastos')
    print('3. Eliminar gasto')
    print('4. Modificar gasto')
    print('5. Ver total de gastos')
    print('6. Salir')
    return input('\nSeleccione una opción: ')


def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            try:
                gasto = float(input('Ingrese el monto del gasto: '))
                gastos.append(gasto)
                print(f'Éxito: gasto de {gasto} agregado.')
            except ValueError:
                print('Error: ingrese un monto numérico.')

        elif opcion == '2':
            if gastos:
                print('Gastos actuales:')
                for i, gasto in enumerate(gastos, start=1):
                    print(f'{i}. {gasto}')
                print('Éxito: gastos mostrados.')
            else:
                print('No hay gastos registrados.')

        elif opcion == '3':
            try:
                indice = int(input('Ingrese el número del gasto a eliminar: ')) - 1
                if 0 <= indice < len(gastos):
                    eliminado = gastos.pop(indice)
                    print(f'Éxito: gasto de {eliminado} eliminado.')
                else:
                    print('Error: gasto no encontrado.')
            except ValueError:
                print('Error: ingrese un número entero válido.')

        elif opcion == '4':
            try:
                indice = int(input('Ingrese el número del gasto a modificar: ')) - 1
                if 0 <= indice < len(gastos):
                    nuevo_gasto = float(input('Ingrese el nuevo monto del gasto: '))
                    gastos[indice] = nuevo_gasto
                    print(f'Éxito: gasto modificado a {nuevo_gasto}.')
                else:
                    print('Error: gasto no encontrado.')
            except ValueError:
                print('Error: ingrese números válidos.')

        elif opcion == '5':
            print(f'Total de gastos: {sum(gastos)}')

        elif opcion == '6':
            print('Saliendo de la aplicación.')
            break

        else:
            print('Error: opción inválida. Intente nuevamente.')


if __name__ == '__main__':
    main()