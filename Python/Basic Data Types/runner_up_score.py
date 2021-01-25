if __name__ == '__main__':
    msg = '1 -1 -2 -1'
    arr = map(int, msg.split())
    arr = list(arr)
    first = max(arr)
    second = min(arr)
    for v in arr:
        print(f'Array value: {v}')
        if second < v < first:
            second = v
    print(second)
