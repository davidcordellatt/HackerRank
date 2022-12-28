consultas = int(input())

for conjuntos in range(consultas):

    values_a = int(input())

    list_values_a = list(map(int,input().strip().split()))

    values_b = int(input())

    list_values_b = list(map(int,input().strip().split()))
    
    print(set(list_values_a) <= set(list_values_b))