range_countries = int(input())

countries = []

for _ in range(range_countries):
    aux = input()
    countries.append(aux)

print(len(set(countries)))