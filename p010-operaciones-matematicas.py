# p020-operaciones-matematicas.py 
# Demostrar el uso de operadores aritmeticos

print("\033[2J\033[H", end="")
print('-' * 50)
print("Calculadora de Operaciones Matematicas")
print('-' * 50)


x = float(input('Valor de x : '))
y = float(input('Valor de y : '))


suma = x + y
resta = x - y
multi = x * y
divi = x / y
modu = x % y
pot = x ** y
dive = x // y

print('Resultado de las operaciones realizadas \n')
print('-' * 50)
print(f'Numeros {x}, {y}')
print(f'Suma    : {suma:>20.3f}')
print(f'Resta   : {resta:>20.3f}')
print(f'Mult    : {multi:>20.3f}')
print(f'Divi    : {divi:>20.3f}')
print(f'Modu    : {modu:>20.3f}')
print(f'Pot     : {pot:>20,.3f}')
print(f'DivE    : {dive:>20.3f}')
print('-' * 50)
#Con tecla alt + click ponemos mas cursores