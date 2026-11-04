# p144-tabla-multiplicar.py
# Una funcion que imprime la tabla de multiplicar de un numero hasta n

def tabla_multiplicar(tabla:int, hasta:int) -> None:
    """" Imprime la tabla de multiplicar de un numero hasta n """
    print(f'Tabla de multiplicar del {tabla} hasta {hasta}')
    for i in range(1, hasta+1):
        print(f'{tabla} x {i} = {tabla * i} ')

# tabla_multiplicar(3, 12)
tabla = int(input('tabla de multiplicar: '))
hasta = int(input('hasta donde quieres: '))
tabla_multiplicar(tabla, hasta)
