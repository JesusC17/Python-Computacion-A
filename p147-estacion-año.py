# p147-estacion-año.py
# Funcion que regresa la estacion del anio segun el numero del mes

def estacion_anio(mes:int) -> str:
    """" Devuelve la estacion del anio segun el numero del mes"""
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    if mes in [12, 1, 2]:
        return meses[mes] + ' y es Invierno'
    elif mes in [3, 4, 5]:
        return meses[mes] + ' y es Primavera'
    elif mes in [6, 7, 8]:
        return meses[mes] + ' y es Verano'
    elif mes in [9, 10, 11]:
        return meses[mes] + ' y es Otonio'

input = int(input('Dame el numeor del mes (1-12): '))
print(f'Corresponde a: {estacion_anio(input)}')
