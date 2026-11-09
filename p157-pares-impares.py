# p157-pares-impares.py
# Recibe una lista de unmeros y regresa 2 listas, unad epares, otra de impares

def separar_pares_impares(lista: list[int]) -> tuple[list[int], list[int]]:
    """ Regresa dos listas, una con los numeros pares y otra con los impares de la lista original """
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Main 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = separar_pares_impares(numeros)
print(f'Los numeros pares de la lista {numeros} son: {pares}')  
print(f'Los numeros impares de la lista {numeros} son: {impares}')