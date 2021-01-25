#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.


def countingValleys(n, s):
    valley = 0
    deep = 0
    is_valley = False

    for c in s:
        if c == 'D':
            deep += 1
        elif c == 'U':
            deep -= 1
        if deep >= 1 and is_valley is False:
            is_valley = True
            valley += 1
        if deep == 0:
            is_valley = False
    return valley


if __name__ == '__main__':
    fptr = open('../../../output.txt', 'w')

    n = 10

    s = ['D', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'U', ]

    result = countingValleys(n, s)

    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
