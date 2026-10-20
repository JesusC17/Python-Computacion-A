# p130-conjunto-personas.py
# Utilidad de conjuntos usando las operaciones y metodos aplicables

A = set()
B = set()

lista_1 = ['Juan','Maria','Pedro','Jose','Rocio']
lista_2 = ['Pedro','Juan','Pablo','Mateo','Esther']

A.update(lista_1)
B.update(lista_2)

print('--- Conjunto A ---')
print(type(A))
print(A)

print('--- Conjunto B ---')
print(type(B))
print(B)

# Union de conjuntos
print('\nUnion de conjuntos')
print(f'(A | B): {A.union(B)}')

# Interseccion de conjuntos
print('\nInterseccion de conjuntos')
print(f'(A & B): {A & B}')

# Diferencia de conjuntos
print('\nDiferencia de conjuntos')
print(f'(A - B): {A - B}')

# Diferencia simetrica de conjuntos
print('\nDiferencia simetrica de conjuntos')
print(f'(A ^ B): {A ^ B}')

print('¿Es {Pablo, Mateo} un subconjunto de B? ', {'Pablo','Mateo'}.issubset(B))

print('¿Es A un superconjunto de {Reynaldo, Angelica}?', A.issuperset({'Reynaldo', 'Angelica'}))

print('¿Está "Pedro" en el conjunto A?', 'Pedro' in A)

print('¿No está "Lilia" en el conjunto B?', 'Lilia' not in B)