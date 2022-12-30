import numpy

X,Y = map(int, input().split())

my_array = numpy.array([input().split() for i in range(X)], int)

print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(round(numpy.std(my_array), 11))