#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s_split = s.split(" ") 
    
    for i in range(len(s_split)):
        s_split[i] = s_split[i].capitalize()
        
    return " ".join(s_split)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
