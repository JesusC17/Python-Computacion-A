# p159-nombres.py
# Funcion que toma 2 listas de nombres y regresa una lista
# 1. nombres que estan en ambas listas
# 2. invertir la lista
# 3. convertir a mayusculas

def capturaNombres() -> list[str]:
    """ Captura una lista de nombres del usuario """
    nombres = []
    while True:
        nombre = input('Ingrese un nombre (o enter para terminar): ')
        if nombre.lower() == '':
            break
        nombres.append(nombre)
    return nombres

def procesaNombres(lista1: list[str], lista2: list[str]) -> list[str]:
    """ Procesa dos listas de nombres y regresa una lista con los nombres que estan en ambas listas, invertida y en mayusculas """
    todos = lista1 + lista2
    invertida = todos[::-1]
    mayusculas = []
    for i in range(len(invertida)):
        mayusculas.append(invertida[i].upper())
    return mayusculas


# Principal
nombres1 = ['Ana','Juan','Pedro','Luis','Maria']
nombres2 = capturaNombres()

print(f'Los nombres de la primera lista son: {nombres1} - len: {len(nombres1)}')
print(f'Los nombres de la segunda lista son: {nombres2} - len: {len(nombres2)}')
todos = procesaNombres(nombres1, nombres2)
print(f'Los nombres de ambas listas, invertidos y en mayusculas son: {todos}')