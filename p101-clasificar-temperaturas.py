# p101-clasificar-temperaturas.py
# Clasifica temperaturas en grados centigrados:Fria, Templada y Calida usando compresion de listas

print('\033[2J\033[H', end='')
print('\033[1;34m' + 'Clasificar temperaturas usando compresion de listas' + '\033[0m')

temp = [0, 15, 22, 28, 35, 40]

# clasificacion de temperatura grados centigrados
clasificacion = ['Fria' if t < 20 else 
                 'Templada' if 20 <= t < 30 else 
                 'Calida' for t in temp]

print('Temperaturas:', temp)
print('Clasificacion:', clasificacion)