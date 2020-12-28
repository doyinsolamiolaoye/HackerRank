n = int(input())
phone_book = {}

for i in range(n):
    name, number = input().split()
    phone_book[name] = number

while True: # this provides for the unknown lines of input
    try: 
        name = input()
        if name in phone_book:
            print("{}={}".format(name,phone_book[name]))
        else:
            print("Not found")
    except:
        break #leaves the for loop  upon exception
