def roman(s):
    sum = 0 
    myDic = {

            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
    }

    i = 0
    while i < len(s): 
        if i != len(s) - 1 and myDic.get(s[i+1]) > myDic.get(s[i]):
            sum = sum + ( myDic.get(s[i+1]) - myDic.get(s[i]) )
            i += 1
        else: 
            sum = sum + myDic.get(s[i])
        i += 1

    return sum

print(roman("III"))