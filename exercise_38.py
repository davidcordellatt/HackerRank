from collections import defaultdict

default = defaultdict(list)
group_1, group_2 = map(int, input().split())
for i in range(group_1):
    default[input()].append(i+1)
for j in range(group_2):
    l = default[input()]
    print(*l) if l else print(-1)