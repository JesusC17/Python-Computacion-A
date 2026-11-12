# p163-suma-pares-impares.py
# Programa que suma numeros pares op impares dentro de un rango. Debe tenr una funcvion que reciba tres parametros, numero de inicio, numero de fin 
# y una letra 'P' o 'I'. Si es P la funcion devulve la suma detodos los pares incluyendo los limites. Si es I devuelve la suma de todos los impares del rango

def sum_par_imp(ini: int, fin: int, op: str ):
    """ Funcion que devulve la suma de pares o impares """
    total = 0
    numeros = []
    if op == 'P':
        for i in range(ini, fin + 1, 1):
            if i % 2 == 0:
                numeros.append(i)
                total += i
        print(f'La suma de los numeros pares entre {ini} y {fin} es: {total}')

    elif op == 'I':    
        for i in range(ini, fin + 1, 1):
            if i % 2 != 0:
                numeros.append(i)
                total += i
        print(f'La suma de los numeros impares entre {ini} y {fin} es: {total}')

    calculo = ' + '.join(str(numero) for numero in numeros)
    print(f'(Cálculo: {calculo} = {total})')

print('* * * Suma en Rango * * *')
n_in = int(input('Introduce el numero inicial: '))
n_fi = int(input('Introduce el numero final: '))
op = input('Que deseas sumar? (P)ares o (I)mpares: ')

sum_par_imp(n_in, n_fi, op)