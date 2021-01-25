#!/bin/python3

import math
import os
import random
import re
import sys

os.environ['OUTPUT_PATH'] = '../../output.txt'


# Complete the solve function below.
def solve(s):
    arr = s.split()
    print(arr)
    for x in arr:
        s = s.replace(x, x.capitalize())
    # return s
    print(s)
    return ' '.join([str(i.capitalize()) for i in s[:].split()])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = '132 456 Wq  m e'

    result = solve(s)

    print(result)

    fptr.write(result + '\n')

    fptr.close()
