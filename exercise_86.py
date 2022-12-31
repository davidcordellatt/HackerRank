from collections import namedtuple
S = int(input())
students = namedtuple('students', input())
print(sum([int(students(*input().split()).MARKS) for _ in range(S)])/S)