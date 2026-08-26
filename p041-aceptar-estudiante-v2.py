# p041-aceptar-estudiante-v2.py
# Programa que determina si un aspirante es aceptado o rechazado
# Sea mujer, mayor de 18 y 

print('\033[2J\033[H', end='')
print('Programa que determina si un aspirante es aceptado o rechazado')

nombre = input('Nombre: ')
sexo = input('Sexo (h/m)')
edad = int(input('Edad: '))
print('Ingresa las tres calificacciones separadas por espacio: ')
cal1, cal2, cal3 = map(float, input().split())

prom = (cal1 + cal2 + cal3) / 3

if sexo == 'm':
    if edad > 21:
        if prom >= 8 and prom <= 9.5:
            print('Aspirante aceptado')
        else:
            print('Aspirante rechazo por tener promedio fuera de rango')
    else:
        print('Aspirante rechazado por ser menor de 21')

    
else:
    print('Aspirante rechazado por ser hombre')