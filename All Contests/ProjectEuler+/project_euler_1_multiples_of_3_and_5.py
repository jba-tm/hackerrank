#!/bin/python3

import sys


def sum_of_multiples(n, limit):
    k = (limit - 1) // n
    return ((n + k * n) * k) // 2


def compute(limit):
    return (
            sum_of_multiples(3, limit) +
            sum_of_multiples(5, limit) -
            sum_of_multiples(15, limit)
    )


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(compute(n))
