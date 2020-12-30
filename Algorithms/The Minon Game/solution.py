def minion_game(string):
    # your code goes here
    scores = {"Kevin" : 0, "Stuart": 0}
    s_length = len(string)
    vowels = 'AEIOU'

    for i in range(s_length):
        if string[i] in vowels:
            scores["Kevin"] += (s_length - i)
        else:
            scores["Stuart"] += (s_length - i)
    
    if scores["Kevin"] > scores["Stuart"]:
        print("Kevin" , scores["Kevin"] )
    
    elif scores["Kevin"] < scores["Stuart"]:
        print("Stuart" , scores["Stuart"])
    
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)