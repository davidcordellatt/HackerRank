n = int(input())

lista_de_enteros = map(int, input().split())
    
hasheable = tuple(lista_de_enteros)

print(hash(hasheable))

# Para entender más sobre hash(), busque las siguientes lecturas:
# https://docs.python.org/3/library/functions.html#hash
# https://interactivechaos.com/en/python/function/hash
# https://ellibrodepython.com/hash-python
