import numpy

x = int(input())

my_array_x = numpy.array([input().split() for i in range(x)], int)
my_array_y = numpy.array([input().split() for i in range(x)], int)

print(numpy.dot(my_array_x, my_array_y))