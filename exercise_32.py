#Iterables and Iterators

input()
letras = input().split()
numero_de_letras = len(letras)
probabilidad = int(input())

letras_a = 0
for i in letras:
    if i == 'a':
        letras_a += 1
        
no_es_a = numero_de_letras - letras_a

probabilidad_negativa = 1

for letra in range(probabilidad):
    if no_es_a > 0:
        probabilidad_negativa *= no_es_a / (no_es_a + letras_a)
        no_es_a -= 1
    else:
        probabilidad_negativa = 0
        break
print(1 - probabilidad_negativa)
