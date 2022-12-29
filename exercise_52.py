num_max = int(input())

for item in range(1,num_max + 1):
    print(*range(1, item), *range(item, 0, -1), sep=dir()[0][0:0])

#sep=dir()[0][0:0] retornará un espacio vacio