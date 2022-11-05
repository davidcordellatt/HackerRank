if __name__ == '__main__':
    alumnos_list = []
    puntos_list = []
    nombres = []
    n = int(input())
    for i in range(n):
        nombre = input()
        puntos = float(input())
        alumnos_list.append([nombre,puntos])
        puntos_list.append(puntos)
            
    puntos_list = sorted(list(set(puntos_list)))
    segunda_puntuacion = puntos_list[1]
    
    for stu in alumnos_list:
        if stu[1] == segunda_puntuacion:
            nombres.append(stu[0])
    
    nombres = sorted(nombres)
    for nombre in nombres:
        print(nombre)