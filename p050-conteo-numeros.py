# p050-conteo-numeros.py
# El ususario introduce n numeros parar con 999, se suman y se cuentan

print('\033[2J\033[H', end='')
print('El ususario introduce n numeros parar con 999, se suman y se cuentan')

c = suma = cp = cn = cz = 0

while True:
    num = int(input('Numero ?'))
    if num == 999: break
    c += 1
    suma += num     #Acumulando
    if num > 0:  
        cp += 1
    elif num < 0: 
        cn += 1
    else: 
        cz += 1

print('\nResumen de los calculos')
print(f'\nCuantos    : {c}')
print(f'\nSuma       : {suma}')
print(f'\nPos        : {cp}')
print(f'\nNeg        : {cn}')
print(f'\nZer        : {cz}')

print('\nProceso terminado')