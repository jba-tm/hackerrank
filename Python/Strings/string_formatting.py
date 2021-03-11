def print_formatted(number):
    width = len(bin(n))-2
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

        # print(int(i), oct(i), hex(i), bin(i), sep=' '.center(5, ' '))


if __name__ == '__main__':
    n = 76
    print_formatted(n)
