range_set = int(input())

this_set = set(map(int, input().split()))

range_actions = int(input())

for _ in range(range_actions):
    
    actions = input().split()
    
    if actions[0] == 'intersection_update':
        aux = set(map(int, input().split()))
        this_set.intersection_update(aux)
    
    if actions[0] == 'update':
        aux = set(map(int, input().split()))
        this_set.update(aux)

    if actions[0] == 'symmetric_difference_update':
        aux = set(map(int, input().split()))
        this_set.symmetric_difference_update(aux)

    if actions[0] == 'difference_update':
        aux = set(map(int, input().split()))
        this_set.difference_update(aux)

print(sum(this_set))