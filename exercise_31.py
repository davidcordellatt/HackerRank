#itertools.permutations(iterable[, r])

from itertools import permutations

texto, cantidad = input().split()
texto = sorted(texto)
cantidad = int(cantidad)

for i in permutations(texto, cantidad):
    print(''.join(i).upper())