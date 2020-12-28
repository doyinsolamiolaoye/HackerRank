if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().strip().split())) #takes the input and splits into a lsit of integer values
    print(' '.join(map(str,arr[::-1])))