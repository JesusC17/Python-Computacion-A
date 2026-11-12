# p164-suma-digitos.py
# Programa que procesa una lista de numeros:
# 1. Funcion que lee y devuelve una lista de numeros enteros
# 2. Una funcion que reciabun numero entero y devuelva la suma de sus digitos individuales (ej: 1971 -> 1+9+7+1 = 18).
# 3. Una función principal que reciba la lista de números. Esta debe usar la función anterior para crear y
#    devolver una nueva lista que contenga la suma de los dígitos de cada número original.

def leer_numeros() -> list[int]:
    """Lee números enteros separados por espacios y los devuelve en una lista."""
    entrada = input('Dame los números (separados por espacio): ')
    return [int(numero) for numero in entrada.split()]

def suma_digitos(numero: int) -> int:
    """Devuelve la suma de los dígitos de un número entero."""
    return sum(int(digito) for digito in str(abs(numero)))

def procesar_lista(numeros: list[int]) -> list[int]:
    """Devuelve una lista con la suma de los dígitos de cada número."""
    return [suma_digitos(numero) for numero in numeros]

def main() -> None:
    numeros = leer_numeros()
    sumas = procesar_lista(numeros)

    print(f'La lista de números original                     : {numeros}')
    print(f'La lista con las suma de dígitos de los números: {sumas}')


if __name__ == '__main__':
    main()