#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    number = len(c)
    while i < number-1:
        if i + 2 >= number or c[i + 2] == 1:
            i += 1
            jumps += 1
        else:
            i += 2
            jumps += 1
    return jumps


if __name__ == '__main__':
    fptr = open('../../../output.txt', 'w')

    n = 6

    # c = [0, 0, 1, 0, 0, 1, 0, ]

    c = [0, 0, 0, 0, 1, 0, ]

    result = jumpingOnClouds(c)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
