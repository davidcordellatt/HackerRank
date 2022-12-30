import re

match = re.search(r'([A-Za-z\d])(?=\1)', input())
print(match[0] if match else -1)

#def repeat(s):
#  count = 0
#  while count < len(s) - 1:
#    if s[count].isalnum():
#      if s[count] == s[count + 1]:
#        print(s[count])
#        break

#      else:
#        count +=1
      
#    else:
#      count +=1

#    if count == len(s) - 1:
#      print(-1)

#repeat('HackerRank')