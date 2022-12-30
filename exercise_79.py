import re

aux = re.findall(r'(?=[^aeiou]([aeiou]{2,})[^aeiou])',input(),re.I)
if aux:
    print(*aux,sep='\n')
else:
    print(-1)