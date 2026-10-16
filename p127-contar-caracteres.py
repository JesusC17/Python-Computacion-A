# p127-contar-caracteres.py
# programa que cuneta caracateres en una cadena de texto usando diccionarios

frec = {}
print('\033c', end='')
mensaje = input('Ingresa una cadena: ')

for caracter in mensaje:
    if caracter not in frec:
        frec[caracter] = 1
    else: 
        frec[caracter] += 1

print('Resultado:\n', frec)