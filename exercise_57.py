N = int(input())

for _ in range(N):
    aux = input()
    if aux.isdigit() and len(aux) == 10:
        if aux[0] == '9' or aux[0] == '8' or aux[0] == '7':
            print('YES')
        else:
            print('NO')
    else:
        print('NO')