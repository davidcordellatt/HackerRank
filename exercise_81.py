import re

p_and = "(?<=[ ])\&\&(?=[ ])"
p_or = "(?<=[ ])\|\|(?=[ ])"

for _ in range(int(input())):
  text = input()
  text = re.sub(p_and, "and", text)
  text = re.sub(p_or, "or", text)
  print(text)