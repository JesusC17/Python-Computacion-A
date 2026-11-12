# p162–medidas-longitud.py
# Programa conversor de unidades de longitud. Muestra un menú y utilizaq dos funciones separadas:
# 1. Funcion que convierte de pulgadas a centimetro (fórmula: $cm = pulgadas \times 2.54$).
# 2. Funcion que convierte de metros a pies  (fórmula: $pies = metros \times 3.281$).

def pul_cen(pul: float) -> float:
    cen = pul * 2.54
    return cen

def met_pies(met: float) -> float:
    pies = met * 3.281
    return pies


print('* * * Conversor de Unidades * * *')
print('1.   Pulgadas a Centimetros')
print('2.   Metros a Pies')
print('3.   Salir')

op = int(input('Elige una opción: '))

if op == 1:
    pul = float(input('Introduce la cantidad en pulgadas: '))
    cent = pul_cen(pul)
    print(f'{pul} pulgadas equivalen a {cent} centímetros.')
elif op == 2:
    mts = float(input('Introduce la cantidad en metros: '))
    pies = met_pies(mts)
    print(f'{mts} metros equivalen a {pies} pies.')
elif op == 3:
    print('Saliendo del programa...')