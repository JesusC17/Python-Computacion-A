# p019-calculo-tiempo.py
# Programa que convierte horas a dias, minutos y segundos

print("\033[2J\033[H", end="")
print('Programa que convierte horas a dias, minutos y segundos\n')

horas = int(input('Ingresa la cantidad de horas: '))

dias = horas / 24
minutos = horas * 60
segundos = minutos * 60

salida =('Resumen de las conversion de hora/s \n'
    f'Dias:     {dias} \n'
    f'Minutos:  {minutos}\n'
    f'Segundos: {segundos}\n'
)

print(salida)