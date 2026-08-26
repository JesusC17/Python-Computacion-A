# p039-numeros-romanos.py
# Programa que muestre el numero equivalente en romano de 1 a 10

print('\033[2J\033[H', end='')
print('Programa que muestre el numero equivalente en romano de 1 a 10')

num = int(input('Ingresa el numero: '))

if num > 0 and num < 11:
    if num == 1:
        print(f'El numero {num} en romano es I')
    elif num == 2:
        print(f'El numero {num} en romano es II')
    elif num == 3:
        print(f'El numero {num} en romano es III')
    elif num == 4:
        print(f'El numero {num} en romano es IV')
    elif num == 5:
        print(f'El numero {num} en romano es V')
    elif num == 6:
        print(f'El numero {num} en romano es VI')
    elif num == 7:
        print(f'El numero {num} en romano es VII')
    elif num == 8:
        print(f'El numero {num} en romano es VIII')
    elif num == 9:
        print(f'El numero {num} en romano es IX')
    else:
        print(f'El numero {num} en romano es X')
else:
    print('Ingresa un numero dentro del rango')