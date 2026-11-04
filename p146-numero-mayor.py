# p146-numero-mayor.py
# Funcion que devuelve un numero mayor de tres

def mayor(a:int, b:int, c:int) -> int:
    """ Devuelve el numero mayor de tres """
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

#mayor = mayor(40, 20,30)
#print(f'El numero mayor es: {mayor}')

print('Dame tres numeros separados por <enter>')
n1, n2, n3 = int(input()), int(input()), int(input())
print(f'El numero mayor es: {mayor(n1, n2, n3)}')

