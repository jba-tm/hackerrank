def minimumSwaps(arr):
    active = True
    # i = 0
    n = len(arr)
    count = 0
    # while active:
    i = 0
    j = 1
    while i < n:
        if arr[i] > arr[j]:
            if i == arr[j]-1 or j == arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                count += 1
            else:
                j += 1

    result = arr
    return result


if __name__ == '__main__':


    arr = [7, 1, 3, 2, 4, 5, 6,]

    result = minimumSwaps(arr)

    # print(result)

