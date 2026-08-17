# p001-hola-mundo.py
# Lee datos y envia saludo

print("Leyendo datos y enviando un saludo")

# Leer datos

nombre = input("Ingresa tu nombre? ")
edad = int(input("Dame la edad? "))
peso = float(input("Dame el peso? "))

print(f"{nombre} bienvenido a python, tu edad es {edad}, tu peso es {peso}")
print(nombre + "bienvenido a python, tu edad es " + str(edad) +", tu peso es " + str(peso))