def print_formatted(number):
    
    espacio = len(bin(number)[2:])
    
    for x in range(1, number + 1):
        print(str(x).rjust(espacio, " "), end=" ")
        print(oct(x)[2:].rjust(espacio, " "), end=" ")
        print(hex(x)[2:].upper().rjust(espacio, " "), end=" ")
        print(bin(x)[2:].rjust(espacio, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)