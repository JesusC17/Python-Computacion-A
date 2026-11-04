# p142-func-mas-param.py
# Ejemplo de funcion que recibe n parametros y los imprime en pantala

def saluda(*nombres:str) -> None:
    for nombre in nombres:
        print(f'Hola {nombre} bienvenido a python, tu nombre tiene {len(nombre)} caracteres')

def edades(*edades:int) -> None:
    print(edades)
    for edad in edades:
        print(f'Tu edad es: {edad} años')

saluda('Jesus Rocha','Juan', 'Pedro')
edades(25,30,40)