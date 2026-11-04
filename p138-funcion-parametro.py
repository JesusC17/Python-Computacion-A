# p138-funcion-parametro.py
# Ejemplo d euna funcion con parametros

def saluda(nombre:str) -> None:
    print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')

saluda('Jesus Rocha Contreras')
saluda('Juan Perez Diaz')
saluda('Maria Soto Garcia')