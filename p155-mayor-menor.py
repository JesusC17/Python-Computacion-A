# p155-mayor-menor.py
# Se crean 2 funciones, una regresa el mayor y otra el menor de una lista d enumeros
# Se crea una funcion mas que captura datos del ususario y regresa una lista de numeros

def captura_numeros() -> list[float]:
    """ Captura numeros del usuario y regresa una lista de numeros"""
    numeros = []
    while True:
        entrada = input("Ingresa un numero (o 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada no valida. Por favor, ingresa un numero.")

    return numeros

def mayor(lista: list[float]) -> float:
    """ Regresa el mayor numero de una lista """
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

def menor(lista: list[float]) -> float:
    """ Regresa el menor numero de una lista """
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor


# Principal
numeros = captura_numeros()
if not numeros:
    print('No se igresaron numeros ')
else:
    print(f'Los numeros capturados son: {numeros}')
    mayor = mayor(numeros)
    print(f'El mayor numero de la lista es: {mayor}')
    menor = menor(numeros)
    print(f'El menor numero de la lista es: {menor}')
