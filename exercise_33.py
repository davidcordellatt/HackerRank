#Maximize It!

a = input().split()
x = input().split()
y = input().split() 
z = input().split()

print("Acaso esto: ")

int_a = [int(i) for i in a]
int_x = [int(i) for i in x]
int_y = [int(i) for i in y]
int_z = [int(i) for i in z]


resultado_esperado = ((int_x[1] ** 2) + (int_y[3] ** 2) + (int_z[5] ** 2) % int_a[1])


print("El resultado es:", resultado_esperado)

print("No es lo mismo a que haga esto: ")

int_a.sort()
int_x.sort()
int_y.sort()
int_z.sort()

resultado_cambiado = ((int_x[-1] ** 2) + (int_y[-1] ** 2) + (int_z[-1] ** 2) % int_a[-1])
print("El resultado entonces es:", resultado_cambiado)

#Este fue uno de los intentos.

listas_de_numeros, divisor_maximo = input().split()

listas_de_numeros = int(listas_de_numeros)
divisor_maximo = int(divisor_maximo)
dividendos = []
str_producto = ""

while len(dividendos) < listas_de_numeros:

    numeros = input().split()

    int_numeros = [int(i) for i in numeros if i > 10]
    int_numeros = list(set(int_numeros))
    int_numeros.sort()
    
    dividendos.append(int_numeros[-1] ** 2)
    

if len(dividendos) == listas_de_numeros:
    producto = sum(dividendos) % divisor_maximo
    str_producto = str(producto)
    print(str_producto)

#HackerRank:
from itertools import product

listas_de_numeros, divisor_maximo = input().split()

listas_de_numeros = int(listas_de_numeros)

divisor_maximo = int(divisor_maximo)

numeros = [[int(numero)**2 for numero in input().split()] for _ in range(listas_de_numeros)]

result = max(sum(i) % divisor_maximo for i in product (*numeros))

print(result)