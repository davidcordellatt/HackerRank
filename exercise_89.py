from collections import deque

range_actions = int(input())
number = deque()

for _ in range(range_actions):
  aux = input().split()

  if aux[0] == 'append':
    number.append(aux[-1])

  if aux[0] == 'appendleft':
    number.appendleft(aux[-1])

  if aux[0] == 'pop':
    number.pop()

  if aux[0] == 'popleft':
    number.popleft()

for e in number:
  print(e, end=" ")