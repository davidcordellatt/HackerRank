zapatos = int(input())

inventario = input().split()

ventas = int(input())

compras = []

for _ in range(ventas):
    pedido = input().split()
    compras.append(pedido)

total = 0
revision = 0

while revision < len(compras):
    if compras[revision][0] in inventario:
        inventario.pop(inventario.index(compras[revision][0]))
        total += int(compras[revision][1])
        print(f'Está, se suma {compras[revision][0]}')
        print(f'Van {total}')
        revision += 1
    else:
        revision += 1

print(total)

#https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true