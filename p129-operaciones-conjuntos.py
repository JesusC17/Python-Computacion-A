# p129-operaciones-conjuntos.py

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

print('\033c', end='')

print('Conjunto Base: ')
print(f'c1 :{c1}')
print(f'c2 :{c2}')
print(f'c3 :{c3}')
print(f'c4 :{c4}')

# Union de conjuntos
print('\nUnion de conjuntos')
print(f'c1 U c2: {c1.union(c2)}')
print(f'c1 U c3: {c1 | c3}')

# Interseccion de conjuntos
print('\nInterseccion de conjuntos')
print(f'c1 n c2: {c1.intersection(c2)}')
print(f'c1 n c3: {c1 & c3}')

# Diferencia de conjuntos
print('\nInterseccion de conjuntos')
print(f'c1 - c2: {c1.difference(c2)}')
print(f'c2 - c3: {c2 - c3}')

# Diferencia simetrica de conjutos
print('\nDiferencia simetrica de conjutos')
print(f'c1 -s c2: {c1.symmetric_difference(c2)}')
print(f'c2 -s c3: {c2 ^ c3}')

# Subconjuntos 
print('\nSubconjuntos')
print(f'c4 es subconjunto de c1? {c4.issubset(c1)}')
print(f'c3 es superconjunto de c2? {c3.issuperset(c2)}')

# Superconjuntos
print('\nSuperconjuntos')
print(f'c1 es superconjunto de c4? {c1.issuperset(c4)}')
print(f'c2 es superconjunto de c3? {c2.issuperset(c3)}')

# Pertenencia y no pertenencia
print(f"¿Está el 2 en c1? : {2 in c1} (True)")
print(f"¿No está el 6 en c1? : {6 not in c1} (True)")