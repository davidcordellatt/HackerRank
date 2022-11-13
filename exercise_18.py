def split():
    text = input("text: ")
    split_text = text.split()
    join_text = "-".join(split_text)
    print(join_text)
    
if __name__ == '__main__':
    split()

##En HackerRank es así:

def split_and_join(line):
    split_text = line.split()
    result = "-".join(split_text)
    return result
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)