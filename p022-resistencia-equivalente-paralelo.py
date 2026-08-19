# p022-resistencia-equivalente-paralelo.py
# Programa que calcula la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo.

print("\033[2J\033[H", end="")
print('Programa que calcula la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo. \n')

print('Ingresa los valores de las 4 resistneicas separados por espacio: ')
r1, r2, r3, r4 = input().split()
r1, r2, r3, r4 = int(r1), int(r2), int(r3), int(r4)

resTotal = 1 / ( (1/r1) + (1/r2) + (1/r3) + (1/r4) )

print(f'La resistencia total es de {resTotal:.2f} ohms')