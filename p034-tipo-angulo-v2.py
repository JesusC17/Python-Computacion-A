# p034-tipo-angulo-v2.py
# Dado un angulo en el rango de 0 a 360 indicar que tipo de angulo es 

print("\033[2J\033[H", end="")
print('Dado un angulo en el rango de 0 a 360 indicar que tipo de angulo es')

ang = int(input('Angulo? '))

if ang < 0 and ang > 360:
    print('\nAngulo fuera de rango')
else:
    print('Tu angulo es: ' , end='')
    if ang < 90: 
        print('AGUDO') 
    elif ang == 90: 
        print('RECTO')
    elif ang < 180: 
        print('OBTUSO')
    elif ang == 180: 
        print('LLANO')
    elif ang < 360: 
        print('CONCAVO')
    elif ang == 360: 
        print('CERRADO')

print('\nProceso terminado')