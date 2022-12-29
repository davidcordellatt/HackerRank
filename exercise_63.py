from numpy import zeros, ones

tridimentional = list(map(int, input().split()))

print(zeros(tridimentional, dtype=int), ones(tridimentional, dtype=int), sep='\n')