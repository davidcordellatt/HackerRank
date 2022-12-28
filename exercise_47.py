x = int(input())

set_1 = input().split()

repeat = set()

diference = set()

for i in set_1:
    if i not in repeat:
        repeat.add(i)
        diference.add(i)
    else:
        diference.discard(i)
diference=list(diference)
print(diference[0])