if __name__ == '__main__':
    n = 2
    numbers = '2 3'
    integer_list = map(int, numbers.split())
    t = tuple(integer_list)
    print(hash(t))

