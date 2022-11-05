if __name__ == '__main__':
    i = int(input())
    j = int(input())
    k = int(input())
    
    n = int(input())
    res=[]
    for i in range(i+1):
        for j in range(j+1):
            for k in range(k+1):
                if i+j+k !=n:
                    res.append([i,j,k])
    print(res)