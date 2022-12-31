from collections import Counter
words_list=[]
W =int(input())
for _ in range(W):
    words_list += [input()]
words_list = Counter(words_list).items()
print(len(words_list))
for key , value in words_list :
    print(value , end=' ')