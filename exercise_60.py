op = int(input())

for _ in range(op):

    x, y = input().split()
    
    if x.isdigit() and y.isdigit():

        x = int(x)
        y = int(y)
        if y > 0:
            print(round(x / y))
        else:
            print('Error Code: integer division or modulo by zero')

    else:

        if not x.isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{x}'")
        
        if not y.isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{y}'")