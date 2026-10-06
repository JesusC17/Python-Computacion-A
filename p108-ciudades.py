# p108-ciudades.py
# Lee nombres de ciudades en una lista, continuando hasta que el usuario introduzca el caracter $
# Imprime: La lista completa, lista ordenada en orden descendente, cuantas ciudades inician con
# letra consonante y sus nombre

ciudades = []
ciudades_cons = []
vocales = "aeiou"

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Lee nombres de ciudades y dice cuantas inician con consonante' + '\033[0m')


while True:
    city = input('Introduzca nombre de ciudad ($ para detener): ')
    if city == '$':
        break
    else:
        ciudades.append(city)
        primera_letra = city[0].lower()
        if primera_letra.isalpha and primera_letra not in vocales:
            ciudades_cons.append(city)

print('--- Resultados ---')
print('Total de ciudades introducidas: ', len(ciudades))
print('Lista original: ',ciudades)
ciudades.reverse()
print('Lista ordenada descendente: ', ciudades)
print('Ciudades que inician con consonante: ', len(ciudades_cons))
print('Lista de ciudades con consonante inicial: ', ciudades_cons)

