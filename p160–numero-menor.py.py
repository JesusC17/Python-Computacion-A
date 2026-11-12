# p149–numero-menor.py
# Programa que pide 3 numeros y mediante una funcion devuelve el numero menor

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
n3 = int(input('Ingrese el tercer numero: '))

def menor(n1: int, n2: int, n3: int) -> int:
    """ Regresa el numero menor de 3 numeros """
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3

# principal
men = menor(n1, n2, n3)
print(f'El numero menor ingresado es {men}')