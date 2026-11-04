# p151-promedio-letra.py
# Dado un promedio regreasr la letra correspondiente y un mensaje
#Entre 90 y 100, A, Excelente
# Entre 80 y 90, B, Muy bien
# Entre 70 y 80, C, Suficiente
# Entre 60 y 70, D, Insuficiente
# Menor a 60, F, Reprobado

def promedio_a_letra(promedio:float) -> tuple[str, str]:
    """ Regresa la letra correspondiente al promedio y un mensaje """
    letra = ''; mensaje = ''
    if promedio >= 90 and promedio <= 100:
        letra = 'A'
        mensaje = 'Excelente'
    elif promedio >= 80 and promedio < 90:
        letra = 'B'
        mensaje = 'Muy bien'
    elif promedio >= 70 and promedio < 80:
        letra = 'C'
        mensaje = 'Suficiente'
    elif promedio >= 60 and promedio < 70:
        letra = 'D'
        mensaje = 'Insuficiente'
    else:
        letra = 'F'
        mensaje = 'Reprobado'

    return letra, mensaje

def main() -> None:
    promedio = float(input('Dame el promedio: '))
    letra, mensaje = promedio_a_letra(promedio)
    print(f'El promedio {promedio} corresponde a la letra {letra} y el mensaje es: {mensaje}')

if __name__ == '__main__':
    main()