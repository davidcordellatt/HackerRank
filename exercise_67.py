import numpy

X,Y = map(int, input().split())

my_array = numpy.array([input().split() for i in range(X)], int)
  
print(numpy.prod(numpy.sum(my_array, axis = 0)))