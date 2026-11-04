# p139-funcion-parametros.py
# Ejemplo de funcion con varios parametros

def saluda(apaterno:str, nombre:str) -> None:
    print(f'Hola {nombre} {apaterno}')

saluda('Rocha','Jesus')
# saluda('Jesus Rocha Contreras') da error porque le falta parametro
# saluda('Jesus', 'Rocha', 'Contreras') da error porque son mas parametros