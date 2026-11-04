# p150-factorial.py
# funcion que calcula el factorial de un numero

def factorial(n:int) -> int:
    """ Regresa el factorial de un numero entero """
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def main() -> None:
    print('Dame un numero entero: ')
    n = int(input())
    print(f'El factorial de {n} es: {factorial(n)}')

if __name__ == '__main__':
    main()