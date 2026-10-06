# p110-comprension-filtra-palabras.py
# De una lista de palabras introducidas separadas por espacio,  filtrar las que tiene 
# mas de 4 caracteres y imprimirlas en mayusculas

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Imprime ne mayuscula aquellas palabras de mas de 4 caracteres introducidas' + '\033[0m')

palabras = input("Introduzca palabras separadas por espacios: ").split()

# Filtrar palabras con más de 4 caracteres y convertirlas a mayúsculas
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 4]

# Imprimir los resultados
print("\n--- Resultados ---")
print("Lista original:", palabras)
print("Lista filtrada (>4 caracteres y en MAYÚSCULAS):", palabras_filtradas)