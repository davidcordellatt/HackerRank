def minion_game(string):
    vowels = "aeiou"
    kevin_points = 0
    stuarts_point = 0
    n = len(string)
    for i in range(n):
        letter = string[i].lower()
        letter_remaining = n - i
        if letter in vowels:
            kevin_points += letter_remaining
        else:
            stuarts_point += letter_remaining
            
    if stuarts_point == kevin_points:
        print('Draw')
    
    elif stuarts_point > kevin_points:
        print('Stuart', stuarts_point)
        
    else:
        print('Kevin', kevin_points)

if __name__ == '__main__':
    s = input()
    minion_game(s)