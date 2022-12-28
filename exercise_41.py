x, y = input().split()

conjunto_felicidad = list(map(int, input().split()))

A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = [1 for i in conjunto_felicidad if i in A]

unhappiness = [-1 for i in conjunto_felicidad if i in B]

print(sum(happiness + unhappiness))