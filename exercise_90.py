n,x=input().split()

values = []

averages = []

for i in range(int(x)):
    aux = list(map(float,input().split()))
    values.append(aux)

averages = zip(*values)
for i in averages: 
    print(sum(i)/int(x))