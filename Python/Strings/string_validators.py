if __name__ == '__main__':
    s = input()
    # uses all five string methods on each character in input string
    # prints True if at least one character made the method return True
    print("\n".join([str(any(i)) for i in
                     (list(zip(
                         *[[c.isalnum(), c.isalpha(), c.isdigit(), c.islower(), c.isupper()] for c in s])))])
          )
