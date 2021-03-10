import textwrap


def wrap(text, n):
    # return [text[i:i + n] for i in range(0, len(text), n)]
    return '\n'.join(textwrap.wrap(text, width=n, ))


if __name__ == '__main__':
    string, max_width = 'fasdadfadsafdasfdsfdsafdsadfsadfs', 6
    result = wrap(string, max_width)
    print(result)
