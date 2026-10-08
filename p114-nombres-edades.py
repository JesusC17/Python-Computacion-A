# p114-nombres-edades.py
# Censo de nombres y edades en un diccionario, hasta <Enter> vacio

print('\033c',end='')

# Crear diccionario
censo = {}

# Solicitar al usuario que igrese los datos
while True:
    nombre = input('Ingrese un nombre (o presione <Enter>) para salir: ')
    if nombre == '':
        break
    censo[nombre] = int(input(f'Ingrese la edad de {nombre}: '))

# Mostrar el contenido
print(f'Censo de nombres y edades: {censo} - {len(censo)} elementos')

# Resumen del censo
print('Resumen del censo: ')
total_edades = 0
for nombre, edad in censo.items():
    print(f'- {nombre}: {edad} años')

suma_edades = sum(censo.values())
promedio_edades = suma_edades / len(censo) if censo else 0
print(f'Suma de edades: {suma_edades} anios')
print(f'Promedio de edades: {promedio_edades:.2f} anios')