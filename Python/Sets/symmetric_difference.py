if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    # n = 4
    # a = set(map(int, '2 4 5 9'.split()))
    # m = int(4)
    # b = set(map(int, '2 4 11 12'.split()))
    for i in sorted(list(a.difference(b)) + list(b.difference(a))):
        print(i)
