if __name__ == '__main__':

    a, b = [int(x) for x in input().split()]
    modelo = ".|."
    for i in range(1,a,2):
        print((modelo*i).center(b, "-"))
    
    print("WELCOME".center(b, "-"))

    for i in range(a-2,0,-2):
        print((modelo*i).center(b, "-"))