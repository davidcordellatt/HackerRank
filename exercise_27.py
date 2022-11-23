from string import ascii_lowercase

def print_rangoli(size):
    abc = ascii_lowercase[:size][::-1]
    rangoli_matrix = []
    
    for i in range(size):
        letters = abc[:i+1][::-1]
        row = []
        k = 0
        
        for j in range(size * 2 -1):
            if k < len(letters) and j % 2 == 0:
                row.append(letters[k])
                k +=1
                
            else:
                row.append('-')
                
        row = ''.join(row[::-1]) + ''.join(row[1:])
        print(row)
        rangoli_matrix.append(row)
    
    rangoli_matrix.pop()
    for r in rangoli_matrix[::-1]:
        print(r)
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)