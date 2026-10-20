# p131-conjunt-numeros.py
#

lista_1 = [50, 60, 70, 80, 90, 100, 200]
lista_2 = [60, 90, 100, 300, 400, 500]
lista_3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista_1)
B = set(lista_2)
C = set(lista_3)

print('--- Conjunto A ---')
print(type(A))
print(A)

print('--- Conjunto B ---')
print(type(B))
print(B)

print('--- Conjunto C ---')
print(type(C))
print(C)

print('\nUnión (A | B): ', A.union(B))

print('\nUnión (B | C): ', B | C)

print('\nDiferencia (A - C): ', A.difference(C))

print('\nDiferencia Simétrica (B ^ C): ',B.symmetric_difference(C))

print('\nIntersección (B & C): ', B.intersection(C))

print('\n¿Es A subconjunto de B? ', A.issubset(B))
print('\n¿Es C subconjunto de A? ', C.issubset(A))
print('\n¿Está el número 100 en A? ', 100 in A)
print('\n¿Está el número 60 en A, B y C? ', 60 in A and 60 in B and 60 in C )
print('\n¿No está el número 900 en C? ', 900 not in C)