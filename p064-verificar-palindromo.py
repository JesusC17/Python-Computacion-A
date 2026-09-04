# p064-verificar-palindromo.py
# Programa que determina si un numero es palindromo

print('\033[2J\033[H', end='')
print('Programa que determina si un numero es palindromo')

while True:
    n = input('Introduce un numero para verificar si es palindromo: ')
    ca = 0 #asendente
    cd = 1 #contador desendente
    while True:
        if not n[ca] == n[len(n) - cd]: 
            print(f'El numero {n} no es un palindromo \n')
            break
        ca += 1
        cd += 1
        if ca >= len(n) // 2: 
            print(f'El numero {n} es un palindromo \n')
            break
    if input('\nDeseas Continuar (S/N)? ').upper() == 'N': break    
print('\nTerminamos...')   