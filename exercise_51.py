from math import degrees, atan

side_AB = int(input())
side_BC = int(input())

print(round(degrees((atan(side_AB / side_BC)))),chr(176),sep='')

# degrees() : Convierte el ángulo x de radianes a grados

# atan() : Retorna la arcotangente de x, en radianes. El resultado está entre -pi/2 y pi/2

# chr(176) retornará °