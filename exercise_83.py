import re

q_range = int(input())
p_float = '^[-+]?\d*\.\d{1,}$'

for _ in range(q_range):
    if re.match(p_float, input()):
        print(True)
    else:
        print(False)