# p153-suma-lista.py
# Funcion para sumar los elementos de una lista

def suma_lista(lista: list[float]) -> float:
    """ Suma los elementos d ena lista de numeros"""
    suma = 0
    for numero in lista:
        suma += numero
    # No se recomienda modificar la lista original
    return suma

# Programa principal
numeros = [1.5, 2.3, 3.7, 4.1, 10.22]
resultado = suma_lista(numeros)
print(f'La suma de los elementos de la lista {numeros} es: {resultado}')
