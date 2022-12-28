range_set = int(input())

this_set = set(map(int, input().split()))

range_actions = int(input())

for _ in range(range_actions):
    
    actions = input().split()
    
    if actions[0] == 'pop':
        this_set.pop()
    
    if actions[0] == 'remove':
        this_set.remove(int(actions[1]))

    if actions[0] == 'discard':
        this_set.discard(int(actions[1]))

print(sum(this_set))