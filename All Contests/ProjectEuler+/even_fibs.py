import sys


def all_fibs(limit=None):
    a = b = 1
    while limit is None or a < limit:
        yield a
        a, b = b, a + b


def even_fibs(m):
    return (f for f in all_fibs(m) if f % 2 == 0)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(even_fibs(n)))
