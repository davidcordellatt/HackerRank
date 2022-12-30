import numpy

numpy.set_printoptions(legacy='1.13')

X, Y = map(int,input().split())
print(numpy.eye(X,Y,k=0))