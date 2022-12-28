x = int(input())

set_1 = set(input().split())

y = int(input())

set_2 = set(input().split())

total = set_1.union(set_2)

print(len(total))