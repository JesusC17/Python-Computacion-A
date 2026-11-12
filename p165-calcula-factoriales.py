# p165-calcula-factoriales.py
# Programa que calcula el factorialde cada numero en una lista. Se debe usar:
# 1. Funcion que lea y devuelva una lisra de nuemros enteros
# 2. Funcion que reciba un numnero entero y devuelva su factorial (ej:5 -> 120)
# 3. Funcion principal que recibe la lista de numeros. Debe suar la funcion factorial para crear u devolver una nueva
#    lista con los factoriales de cada número.

def leer_numeros() -> list[int]:
    """Lee números enteros separados por espacios y devuelve una lista."""
    entrada = input('Dame los números (separados por espacio): ')
    numeros = []

    for numero in entrada.split():
        numeros.append(int(numero))
    return numeros


def factorial(n:int) -> int:
    """ Regresa el factorial de un numero entero """
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def calcular_factoriales(numeros: list[int]) -> list[int]:
    """Devuelve una nueva lista con el factorial de cada número."""
    numeros_fact = []

    for numero in numeros:
        numeros_fact.append(int(factorial(numero)))
        
    return numeros_fact


def main() -> None:
    numeros = leer_numeros()
    factoriales = calcular_factoriales(numeros)

    print(f'La lista de números originales: {numeros}')
    print(f'La lista con los factoriales: {factoriales}')


if __name__ == '__main__':
    main()
