from itertools import combinations as cmb

def run():

    word, number = input().split()
    number = int(number)
    word = ''.join(word)
    for i in range(1,number + 1):
        for i in list(cmb( word, i)):
            # Si colocamos la linea de codigo:
            # if len(i) == number:
            # imprimiria solo las combinaciones con el numero que le indicamos.
            print("".join(i))

if __name__ == '__main__':
    run()