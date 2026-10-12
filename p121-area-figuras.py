# p121-area-figuras.py
# Calculadora dinámica de áreas de figuras geométricas

import math

# Diccionario de diccionarios con la información de cada figura
figuras = {
    "circulo": {
        "parametros": ["radio"],
        "formula": "math.pi * radio ** 2"
    },
    "triangulo": {
        "parametros": ["base", "altura"],
        "formula": "base * altura / 2"
    },
    "rectangulo": {
        "parametros": ["base", "altura"],
        "formula": "base * altura"
    }
}


def mostrar_menu():
    print("Figuras disponibles:")
    for indice, nombre in enumerate(figuras, start=1):
        print(f"{indice}. {nombre.title()}")


def obtener_figura(opcion):
    if opcion == "salir":
        return None

    if opcion in figuras:
        return opcion

    if opcion.isdigit():
        indice = int(opcion) - 1
        nombres = list(figuras.keys())
        if 0 <= indice < len(nombres):
            return nombres[indice]

    return None


while True:
    mostrar_menu()
    opcion = input("Elija una figura (o 'salir' para terminar): ").strip().lower()
    figura = obtener_figura(opcion)

    if figura is None and opcion != "salir":
        print("Opción inválida. Intente nuevamente.")
        continue

    if figura is None:
        print("Fin del programa.")
        break

    datos = {}
    for parametro in figuras[figura]["parametros"]:
        valor = float(input(f"Ingrese el valor de {parametro}: "))
        datos[parametro] = valor

    formula = figuras[figura]["formula"]
    area = eval(formula, {"__builtins__": {}, "math": math}, datos)

    print(f"El área del {figura} es: {area:.2f}")
    print()