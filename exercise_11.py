if __name__ == '__main__':
    e = int(input())
    estudiantes = {}
    for _ in range(e):
        nombres, *line = input().split()
        puntuaciones = list(map(float, line))
        estudiantes[nombres] = puntuaciones
    promedio = input()
    print('%.2f'%(sum(estudiantes[promedio])/3))