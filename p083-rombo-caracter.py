# p083-rombo-caracter.py
# Porgrama que imprime un rombo de altura y anchura n 

print('\033[2J\033[H', end='')
print('Programa que imprime un rombo de altura y anchura n  \n')

a = int(input('Dame un un numero impar para la altura: '))
c = input('Caracter a usar: ')

espacio = caracteres = 0
altura = (a // 2) + 1
for i in range(1, altura+1):
    espacio = altura - i
    caracteres = 2 * i -1
    for e in range(espacio):
        print(' ', end='')
    for j in range(caracteres):
        print(c, end='')
    print()

for i in range(altura - 1, 0, -1):
    espacio = altura - i
    caracteres = 2 * i -1
    for e in range(espacio):
        print(' ', end='')
    for j in range(caracteres):
        print(c, end='')
    print()
