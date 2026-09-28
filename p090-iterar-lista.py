# p090-iterar-lista.py
# Iterar por los elementos de una lista
# 1 por elemento, 2 por indice, 3 por elemento sumando 2, 4 por indice sumando 10, 5 con enumerate


nums = [2, 4, 6, 8, 10, 12, 14, 16]

print('\033[2J\033[H', end='')
print(f'\nIterar por los elementos de una lista: {nums} | Longitud: {len(nums)}')

# Iterar por elemento
print('\nIterar por elemento')  
for num in nums:
    print(num)

# Iterar por indice
print('\nIterar por indice')
for i in range(len(nums)):
    print(f'Índice: {i}, Valor: {nums[i]}')

# Iterar por elemento sumando 2
print('\nIterar por elemento sumando 2')
for num in nums:
    print(num + 2, end=' ')

# Iterar por indice sumando 10
print('\nIterar por indice sumando 10')
for i in range(len(nums)):
    print(f'Índice: {i}, Valor: {nums[i] + 10}')    

# Iterar con enumerate
print('\nIterar con enumerate')
for i, num in enumerate(nums):
    print(f'Índice: {i}, Valor: {num}')

# Elevar cada elemento al cuadrado
print('\nElevar cada elemento al cuadrado')
nums_cuadrados = [num ** 2 for num in nums]
print(f'Lista original: {nums} | Lista actualizada: {nums_cuadrados}')