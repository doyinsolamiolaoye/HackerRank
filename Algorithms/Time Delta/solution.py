a = set(input().split()) #converts the input value from a list to a set; note that .split() converts it to a list

counter, n = 0 , int(input())

for i in range(n):
    b = set(input().split()) #converts the input from list to set
    if a.issuperset(b): #to check if a set is a subset of another set
        counter += 1
    
print(counter == n) #checks if the numbber of input sets is the same as those who pass the superset test