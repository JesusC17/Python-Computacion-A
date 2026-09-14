# p076-piramide-caracter-v2.py


print('\033[2J\033[H', end='')
print('Imprime piramide de caracteres \n')

altura = 6
c = input('Caracter ? ')
espacio = caracteres = 0

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

