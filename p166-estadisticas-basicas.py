# p166-estadisticas-basicas.py
# Programa que calcula estadisticas basicas (poblacionales) para una listra de numero. Debe incluir
# 1. Funcion para leer una lista de numeros enteros
# 2. Funciones eparadas para calcular y devolver cada una de las siguientes estadisticas.
#       Numero mayor, numero menor, media(promedio), varianza poblacional, desviacion etandar poblacional
# El program principal lee la lista e imprime todos los resultados estadisticos de forma clara

def leer_numeros() -> list[int]:
    """Lee números enteros separados por espacios y devuelve una lista."""
    entrada = input('Dame los números (separados por espacio): ')
    numeros = []

    for numero in entrada.split():
        numeros.append(int(numero))
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

def promedio(lista: list[float]) -> float:
    """ Funcion que calcula el promedio de numeros en una lista """
    promedio = 0
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

def varianza(lista: list[float]) -> float:
    """ Funcion que calcula la varianza poblacional de numeros en una lista """
    prom = promedio(lista)
    suma = 0
    for numero in lista:
        suma += (numero - prom) ** 2
    varianza = suma / len(lista)
    return varianza

def desviacion_estandar(lista: list[float]) -> float:
    """ Funcion que calcula la desviacion estandar poblacional de numeros en una lista """
    var = varianza(lista)
    desviacion = var ** 0.5        # Es igual que sacar la raiz cuadrada 
    return desviacion

def main() -> None:
    numeros = leer_numeros()
    print(f'Lista de números: {numeros}')
    print('Estadísticas:')
    print(f'Media                 : {promedio(numeros):<6.3f}')
    print(f'Mayor                 : {mayor(numeros):<6}')
    print(f'Menor                 : {menor(numeros):<6}')
    print(f'Varianza              : {varianza(numeros):<6.3f}')
    print(f'Desviación estándar   : {desviacion_estandar(numeros):<6.3f}')



if __name__ == '__main__':
    main()