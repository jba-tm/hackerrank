#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def arrayManipulation(arr):

if __name__ == '__main__':
    fptr = open('../../../output.txt', 'w')

    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
