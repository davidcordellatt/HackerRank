#Python
range_group_x = int(input())
group_x = set(input().split())

range_group_y = int(input())
group_y = set(input().split())

output = list(group_x.symmetric_difference(group_y))
output = [int(i) for i in output]
output.sort()

for _ in output:
    print(_)

#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen