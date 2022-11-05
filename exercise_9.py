#Opción 1 para el ejercicios de conseguir al segundo lugar

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    lista_ordenada = list(set(sorted(list(arr))))
    
    print(lista_ordenada[-2])

