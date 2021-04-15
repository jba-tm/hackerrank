from collections import Counter
import itertools

if __name__ == '__main__':
    count = int(input())
    shoes = Counter(map(int, input().split()))
    earn = 0
    customers = int(input())

    for i in range(customers):
        size, price = map(int, input().split())
        if size in shoes.keys():
            if shoes[size] == 0:
                shoes.pop(int(size))
            else:
                shoes[size] -= 1
                earn = earn + price
    print(earn)
