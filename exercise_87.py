from collections import OrderedDict
inventary = OrderedDict()
P = int(input())
for _ in range(P):    
    name,price = input().rsplit(maxsplit=1)    
    inventary[name] = inventary.get(name,0) + int(price)
[print(name,price) for name,price in inventary.items()]