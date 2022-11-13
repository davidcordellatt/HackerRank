#This file if for practice different codes before find the correct answer.

def count_substring(string, sub_string):
    
    count = string.count(sub_string)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

##Tenemos que lograr que el contador cuente elementos ya contados, es decir:
## En el string "ininini" hay 3 "ini", no 2.