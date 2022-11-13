def swap_case():
    s = input("")
    swap_s = s.swapcase() 
    print(swap_s)


if __name__ == '__main__':
    swap_case()

# En HackerRank la forma correcta es así:
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
