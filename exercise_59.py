import re

criterio = ".#[0-9A-Fa-f]{3,6}"

for _ in range(int(input())):
    text = re.findall(criterio, input())
    
    if text:
        for j in text:
            print(j[1:])