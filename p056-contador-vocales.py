# p056-contador-vocales.py
# Dada una frase ceunta las volcales, consonantes y otros

print('\033[2J\033[H', end='')
print('Dada una frase ceunta las volcales, consonantes y otros\n')

frase = input('Introduce una frase: ').lower()
print(f'\nLa frase a analizar es: {frase} y tiene {len(frase)} caracteres')

i = vocal = consonante = otro = 0
while i < len(frase):
    c = frase[i]
    print(c,end='')
    if 'a' <= c <= 'z':
        print(' si')
        if c in 'aeiou':
            vocal += 1
        else:
            consonante += 1
    else:
        print(' no')
        otro += 1
    i += 1

print(f'Vocal:  {vocal}\nConsonantes: {consonante}\nOtros: {otro}')