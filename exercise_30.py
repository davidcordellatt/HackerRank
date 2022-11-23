from itertools import product

if __name__ == '__main__':

    A = input().split()
    B = input().split()

    print(A)
    print(B)

    Ax = []
    Bx = []

    for i in A:
        Ax.append(int(i))
    
    for i in B:
        Bx.append(int(i))

    # print("Lo de abajo es el producto")
    print(*tuple(product(Ax, Bx)))

#Tambien se puede hacer así:

from itertools import product

if __name__ == '__main__':

    A = input().split()
    B = input().split()

    #print(A)
    #print(B)
    
    #print("Arriba es Strings")
    #print("Abajo es Interger")

    A = [int(i) for i in A]
    B = [int(i) for i in B]

    # print(A)
    # print(B)

    # print("Lo de abajo es el producto")
    print(*tuple(product(A, B)))