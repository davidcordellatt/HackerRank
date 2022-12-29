import numpy

X, Y, P = map(int,input().split())

output = []

for _ in range(X + Y):
  output.append(numpy.array(input().split(), int))
output = numpy.asarray(output)
print(output)

