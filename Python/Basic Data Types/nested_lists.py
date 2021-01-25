if __name__ == '__main__':
    n = 5
    temp = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    second_highest = sorted(list(set([marks for name, marks in temp])))
    print([marks for name, marks in temp])
    print('\n'.join([a for a, b in sorted(temp) if b == second_highest]))
