#https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#En HackerRank es:
from itertools import product

k,m = map(int,input().split())

nums = [[int(i)**2 for i in input().split()[1:]] for _ in range(k)]
print(max(sum(i)%m for i in product(*nums)))
