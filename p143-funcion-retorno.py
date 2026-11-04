# p143-funcion-retorno.py
# Funcion que regresa un valor

def suma(a:int, b:int) -> int:
    return a + b

"""res = suma(10,20)
print(res) """

print('Dame dos numeros separados por <enter>')
n1, n2 = int(input()), int(input())
print(f'La suma de {n1} + {n2} es: {suma(n1, n2)}')

