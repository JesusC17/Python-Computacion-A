# p148-temperatura.py
# Permite elegir entre diferentes tipos de conversion de temperatura
# las opciones estan en un meni y s epuede elegir la opcion deseada
# C a F y F a C

def celsius_a_fahrenheit(celsius:float) -> float:
    """ Convierte de Celsius a Fahrenheit """
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit:float) -> float:
    """ Convierte de Fahrenheit a Celsius """
    return (fahrenheit - 32) * 5/9

def main() -> None:
    """ Muestra el menu de opciones """
    while True:
        print('Menu de oversionesd de temperatura')
        print('1. Celsius a Fahrenheit')
        print('2. Fahrenheit a Celsius')    
        print('3. Salir')
        opcion = input('Elige una opcion: ')    
        if opcion == '1':
            celsius = float(input('Dame la temperatura en Celsius: '))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f'{celsius} C = {fahrenheit} F')
        elif opcion == '2':
            fahrenheit = float(input('Dame la temperatura en Fahrenheit: '))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f'{fahrenheit} F = {celsius} C')
        elif opcion == '3':
            print('Saliendo...')
            break
        else:
            print('Opcion no valida. Por favor, elige una opcion valida.')

if __name__ == '__main__':
    main()