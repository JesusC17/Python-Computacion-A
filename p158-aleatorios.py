# p158-aleatorios.py
# Funcion que generea una lista de numeros aleatorios
# Genera 2 listas aletorias usando esa funcion
# Luego obtengo la usma de ambas con otra funcion
import random

def generaAleatorios(n: int, min: int, max: int) -> list[int]:
    """ Genera una lista de n numeros aleatorios entre min y max"""
    lista = []
    for _ in range(n):
        numero = random.randint(min, max)
        lista.append(numero)
    return lista

def sumarListas(lista1: list[int], lista2: list[int]) -> list[int]:
    """ Suma los elementos de dos listas y regres auna nueva lista con los resultados"""
    if len(lista1) != len(lista2):
        return 0
    suma = []
    for i in range(len(lista1)):
        suma.append(lista2[i] + lista1[i])
    return suma

# programa principal
MAX = 10
lista1 = generaAleatorios(MAX, 1, 10)
lista2 = generaAleatorios(MAX, 50, 100)
lista3 = sumarListas(lista1, lista2)

print(f'Lista 1: {lista1}')
print(f'Lista 2: {lista2}')
if lista3 == 0:
    print('Las listas no tienen la misma longitud')
else:
    print(f'Suma de las listas: {lista3}')
    