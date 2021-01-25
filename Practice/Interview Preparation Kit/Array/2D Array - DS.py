#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    # want to find the maximum hourglass sum
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63

    for i in range(4):
        for j in range(4):

            # sum of top 3 elements
            top = sum(arr[i][j:j+3])

            # sum of the mid element
            mid = arr[i+1][j+1]

            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])

            hourglass = top + mid + bottom

            if hourglass > maxSum:
                maxSum = hourglass

    return maxSum




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
