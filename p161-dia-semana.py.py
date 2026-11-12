# p150-dia-semana.py
# Funcion que recibe un numero entero entre 1 y 7, devulve el dia correspondiente de la semana en texto
# El programa principal debe pedir el numero al usuario, llamar la funcion y mostrar el dia.

def dia(num: int) -> str:
    """ Regresa el dia correspondiente segun el numero entre 1 y 7 """
    if num == 1:
        return 'Lunes'
    elif num == 2:
        return 'Martes'
    elif num == 3:
        return 'Miercoles'
    elif num == 4:
        return 'Jueves'
    elif num == 5:
        return 'Viernes'
    elif num == 6:
        return 'Sábado'
    elif num == 7:
        return 'Domingo'
    else:
        return 'Error: El número debe estar entre 1 y 7 '

num = int(input('Introduce un numero del 1 al 7: '))
dia = dia(num)
print(f'El día es: ¨{dia}')
