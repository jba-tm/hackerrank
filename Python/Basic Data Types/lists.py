# if __name__ == '__main__':
#     N = 4
#     commands = []
#     for _ in range(N):
#         input_command = input()
#         commands.append(input_command.split(' '))
#
#     print(commands)


if __name__ == '__main__':
    N = 4
    temp = """insert 0 5
append 9
append 9
append 9
append 9
append 9
print
sort
pop
append 9
reverse
remove 9"""
    commands = []
    lines = temp.split('\n')
    for line in lines:
        commands.append(line.split(' '))
    result = []
    for command in commands:
        current = command[0]
        if current == 'print':
            print(result)
        elif current == 'remove':
            result.remove(int(command[1]))
        elif current == 'sort':
            result.sort()
        elif current == 'pop':
            result.pop()
        elif current == 'append':
            num = int(command[1])
            result.append(num)
        elif current == 'insert':
            result.insert(int(command[1]), int(command[2]))
        elif current == 'reverse':
            result.reverse()

    print(result)
