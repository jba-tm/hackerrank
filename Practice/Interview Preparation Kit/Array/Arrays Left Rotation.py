#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    a=a[(n+d)%n:]+a[0:(n+d)%n]
    return a


if __name__ == '__main__':
    fptr = open('../../../output.txt', 'w')

    # nd = input().split()

    n = 5

    d = 4

    a = [1, 2, 3, 4, 5, ]

    result = rotLeft(a, d)

    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    fptr.close()
