def average(array):
    return sum(set(array))/len(set(array))


if __name__ == '__main__':
    n = 10
    arr = list(map(int, '161 182 161 154 176 170 167 171 170 174'.split()))
    # arr = list(map(int, '154 161 167 170 171 174 176 182'.split()))
    result = average(arr)
    print(result)
