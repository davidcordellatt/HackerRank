import numpy

my_array_x = numpy.array(input().split(), int)
my_array_y = numpy.array(input().split(), int)

print(numpy.inner(my_array_x, my_array_y))
print(numpy.outer(my_array_x, my_array_y))