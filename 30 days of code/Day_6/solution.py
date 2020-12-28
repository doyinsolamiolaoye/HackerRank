n = int(input())

a = 0
while a < n:
    input_string = str(input())
    print(input_string[::2] + " " + input_string[1::2])
    a +=1