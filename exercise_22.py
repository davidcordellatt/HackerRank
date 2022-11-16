if __name__ == '__main__':
    s = input()

    for i in s:
        
        if i.isalnum() == True:
            valor = True
            break

        else:
            valor = False

    print(valor)
        
    for i in s:

        if i.isalpha() == True:
            valor = True
            break

        else:
            valor = False
        
    print(valor)
        
    for i in s:      
        if i.isdigit() == True:
            valor = True
            break

        else:
            valor = False
        
    print(valor)
        
    for i in s:
        if i.islower() == True:
            valor = True
            break

        else:
            valor = False

    print(valor)
        
    for i in s:
        if i.isupper() == True:
            valor = True
            break

        else:
            valor = False

    print(valor)   