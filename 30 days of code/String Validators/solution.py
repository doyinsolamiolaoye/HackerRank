if __name__ == '__main__':
    s = input()
    # print(any(c.isalnum() for c in s))
    # print(any(c.isalpha() for c in s))
    # print(any(c.isdigit() for c in s))
    # print(any(c.islower() for c in s))
    # print(any(c.isupper() for c in s))

    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print( any(method(c) for c in s) )