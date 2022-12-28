def dry(list_strings: list) -> str:
    word = ""
    for letra in list_strings:
        if word == "":
            word = letra
        if word != "":
            if letra not in word:
                word += letra
    return word

def groups(string: str, k: int):

    count = 0
    idx = 0
    words = []

    while count < k:
        aux = ""
        while idx < len(string):
            aux += string[idx]
            idx += 1

            if len(aux) == k:
                words.append(aux)
                aux = ""
        count += 1

    print(words)
    
    dry_words = [dry(i) for i in words]
    print('-----' * 12)
    print(dry_words)


if __name__ == '__main__':
    #Example
    groups("AABCAAADA", 3)

# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true