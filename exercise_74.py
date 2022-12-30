import numpy

def arrays(arr):
    result = numpy.array(arr, float)
    return numpy.flip(result)

arr = [1, 2, 3, 4, -8, -10]
result = arrays(arr)
print(result)