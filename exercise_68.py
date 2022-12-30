import numpy

X,Y = map(int, input().split())

my_array = numpy.array([input().split() for i in range(X)], int)
  
print(numpy.max(numpy.min(my_array, axis = 1)))