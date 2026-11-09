# p156-mayores-promedio.py
# Calcula el promedio de la lista con funcion
# Creamos una lista con los mayores al proemdio con otra funcion

def promedio(lista:list[float]) -> float:
    """ Calcula el promeido de los elementos deuna lista  de numeros """
    suma = 0
    if not lista:
        return 0
    for numero in lista:
        suma += numero
    return suma / len(lista)

def mayores_promedio(lista: list[float], prom: float) -> list[float]:
    """ Regresa una lista con los numeros mayores al promedio de la lista original """
    mayores = []
    for numero in lista:
        if numero > prom:
            mayores.append(numero)
    return mayores


# programa principal
numeros = [12.22, 1.5, 2.3, 3.7, 4.1, 10.22, 34.5]
print(f'Los numeros de la lista son: {numeros}')
prom = promedio(numeros)
print(f'El promedio de los elementos de la lista es: {prom:.2f}')
mayores = mayores_promedio(numeros, prom)
print(f'Los numeros mayores al promedio son: {mayores}')