import numpy

X = int(input())

my_array = numpy.array([input().split() for i in range(X)], float)

print(round(numpy.linalg.det(my_array), 2))