#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a = s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
    return a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('../../../output.txt', 'w')

    s = 'a'

    n = 100000000000000000

    result = repeatedString(s, n)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
