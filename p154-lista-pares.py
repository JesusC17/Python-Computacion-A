# p154-lista-pares.py
# Funcion qu recibe una lista d enumeros enteros y regresa los pares

def lista_pares(lista:list[int]) -> list[int]:
    """ Regresa una lista con los numeros pares de la lista original """
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = lista_pares(numeros)
print(f'Los numeros pares de la lista {numeros} son: {resultado}')