def count_substring(text, substring):
    return (sum([1 for i in range(len(text) - len(substring) + 1)
                 if text[i:i + len(substring)] == substring]))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
