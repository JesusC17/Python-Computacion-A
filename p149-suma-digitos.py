# p149-suma-digitos.py
# funcion que regresa la suma d elos digitos de un numero entero

def suma_digitos(n:int) -> int:
    """ Regresa la suma de los digitos de un numero entero """
    suma = 0
    while n > 0:
        digito = n % 10 # toma el digito de las unidades
        suma += digito
        n //= 10    # elimina el digito de las unidades
    return suma

def main() -> None:
    n = int(input('Dame un numero entero: '))
    print(f'La suma de los digitos de {n} es: {suma_digitos(n)}')   

if __name__ == '__main__':
    main()
    