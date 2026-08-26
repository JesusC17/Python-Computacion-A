# p040-calculo-notas.py
# Programa que calcula el promedio entre 5 calificaciones

print('\033[2J\033[H', end='')
print('Programa que calcula el promedio entre 5 calificaciones')

print('Ingresa 5 calificaciones separadas por espacio: ')
cal1, cal2, cal3, cal4, cal5 = map(float, input().split())

promedio = (cal1 + cal2 + cal3 + cal4 + cal5) / 5

if promedio < 6:
    print('Quedas reprobado')
elif promedio < 7:
    print('Pasas de panzazo')
elif promedio < 8:
    print('Muy bien, puedes mejorar')
elif promedio < 9:
    print('Excelente, sigue asi')
elif promedio < 10:
    print('Perfecto, tu esfuerzo valio la pena')
else:
    print('Ingresa datos correctos')
