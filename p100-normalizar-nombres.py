# p100-normalizar-nombres.py
# De una lista de nombres con espacios y mayusculas, se normalizan los nombres usando compresion de listas a nombres en minusculas y sin epacios al inicio o final

print('\033[2J\033[H', end='')
print('Normalizar nombres usando compresion de listas')

nombres = ['  Juan  ', '  Maria', 'Pedro  ', ' Ana  ', 'Luis', '  Sofia  ']

# Se normalizan los nombres usando compresion de listas
nomres_normalizados = [nombre.strip().lower() for nombre in nombres]

print('Nombres originales:', nombres)
print('Nombres normalizados:', nomres_normalizados)