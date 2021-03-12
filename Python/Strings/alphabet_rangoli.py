# import string
# alpha = string.ascii_lowercase
#
# def print_rangoli(size):
#     # length = (size-1)*4+1
#     # char_int = 96 + size
#     # pattern = [('-'.join(chr(j) for j in range(c-i, char_int+1)[::-1])).center(length, '-') for i, c in enumerate(range(98, char_int+1)[::-1])]
#     # print(pattern)
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
#     print('\n'.join(L[:0:-1] + L))
#     # for i in range(97, char_int+1)[::-1]:
#     #     pattern = [(chr(char_int) * (i - 1)).center(length, '-')]
#     #     print(pattern)
def print_rangoli(n):
    print(4*n-3)
    print((n-1)*4+1)
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")


if __name__ == '__main__':
    n = 27
    print_rangoli(n)
