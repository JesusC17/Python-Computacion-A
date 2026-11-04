# p140-func-param-nombre.py
# Ejemplo de funcion ocn parametros con nombre

def saluda(apaterno:str, amaterno:str, nombre:str) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}')

saluda('Rocha','Contreras','Jesus')
saluda(nombre='Jesus', amaterno= 'Contreras', apaterno='Rocha')
