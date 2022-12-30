import numpy

my_array = []

X, Y = map(int,input().split())

for _ in range(X):
    my_array.append(numpy.array(input().split(), int))
my_array = numpy.asarray(my_array)
print(numpy.transpose(my_array)) 
print(my_array.flatten())