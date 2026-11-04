# p145-cuadro-caracter.py
# Imprime un cuadro de caracteres

def cuadro_caracter(caracter:str, ancho:int, alto:int) -> None:
    """ Imprime un cuadro de caracteres """
    for i in range(alto):
        for j in range(ancho):
            print(caracter, end="")
        print()

cuadro_caracter('*', 10, 5)
caracter = input('Dame un caracter: ')
ancho = int(input('ancho: '))
alto = int(input('alto: '))
print(f'Cuadro de {caracter} de {ancho} x {alto}')
cuadro_caracter(caracter, ancho, alto)