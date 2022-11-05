from itertools import groupby

print(
*[
(
len(list(value)), int(key)) for key, value in groupby(input()
)
]
)