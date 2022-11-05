from itertools import combinations_with_replacement as cmb

def run():

    word, number = input().split()
    number = int(number)
    word = sorted(word)
    for i in (cmb (word, number)):
        print("".join(i))

if __name__ == '__main__':
    run()