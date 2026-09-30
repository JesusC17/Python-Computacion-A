# p097-producto-punto.py
# Cálculo del producto punto de dos vectores

print('\033[2J\033[H', end='') 

# Pedir dos listas de números
vector1 = input("Ingrese el primer vector separado por espacios: ")
vector2 = input("Ingrese el segundo vector separado por espacios: ")

# Convertir los textos a listas de números
vector1 = vector1.split()
vector2 = vector2.split()

# Convertir cada elemento de las listas a entero
for i in range(len(vector1)):
    vector1[i] = int(vector1[i])

for i in range(len(vector2)):
    vector2[i] = int(vector2[i])

# Verificar si tienen la misma longitud
if len(vector1) != len(vector2):
    print("Error: los vectores deben tener la misma longitud.")
else:
    producto_punto = 0

    # Calcular el producto punto
    for i in range(len(vector1)):
        producto_punto += vector1[i] * vector2[i]

    # Mostrar el resultado final
    print("El producto punto es:", producto_punto)

