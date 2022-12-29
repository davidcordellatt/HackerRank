num_max = 5  #int(input())

for num in range(1, num_max):
    print(int(str(num) * int(num)))

# Without str:
print('-----' * 12)

for num in range(1, num_max):
    print(int(num * 10**num // 9))