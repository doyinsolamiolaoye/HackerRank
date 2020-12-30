from datetime import datetime as datetime

def time_delta(t1, t2):
    fmt = '%a %d %b %Y %H:%M:%S %z' #format of the input value
    t1 = datetime.strptime(t1, fmt) #use the strptime method in the datetime module to convert the innput string to date time format
    t2 = datetime.strptime(t2, fmt) 
    diff = (t2-t1).total_seconds()  #.total_seconds() method is used to  
    return str(abs(int(diff)))

t = int(input()) # t holds the number of testcases

for t_itr in range(t): # carry out the body of this code for each test case
    t1 = input()

    t2 = input() # accepts the two time stamps, t1 and t2

    delta = time_delta(t1, t2) #applies the time_delta function on both time stamps

    print(delta + '\n')