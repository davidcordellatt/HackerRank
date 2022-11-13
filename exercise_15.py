N = int(input("Cuantas vueltas dar: "))

lista = []

for num in range(N):

    w = input("").split()

    if w[0] == 'insert':
        lista.insert(int(w[1]), int(w[2]))
    
    if w[0] == 'remove':
        lista.remove(int(w[1]))

    if w[0] == 'append':
        lista.append(int(w[1]))
    
    if w[0] == 'sort':
        lista.sort()

    if w[0] == 'pop':
        lista.pop()

    if w[0] == 'reverse':
        lista.reverse()
    
    if w[0] == 'print':
        print(lista)
