import numpy

X, Y = map(int,input().split())

A = numpy.array([input().split() for _ in range(X)], int)
B = numpy.array([input().split() for _ in range(X)], int)

print(A+B)
print(A-B)
print(A*B) 
print(A//B)
print(A%B) 
print(A**B)