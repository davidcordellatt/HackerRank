set_1 = set(input().split())

result = True

for _ in range(int(input())):

    set_2 = set(input().split())

    if len(set_1 - set_2) == 0:
        result = False

    elif len(set_2 - set_1) > 0:
        result = False 
        
print(result)