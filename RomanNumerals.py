valueDict = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

valueDict2 = {'IV': 4,
             'IX': 9,
             'XL': 40,
             'XC': 90,
             'CD': 400,
             'CM': 900,}

def romanValue(test):
    sum = 0
    for key in valueDict2:
        if key in test:
            sum = sum + valueDict2[key]
            test = test.replace(key,'')

    test = list(test)
    for items in test:
        sum = sum + valueDict[items]

    print(test)
    print(sum)

    return sum

    # for i in range(len(test)-1,-1,-2):
    #     #print(test[i])
    #     p1 = test[i]
    #     p2 = test[i-1]
    #     print(p1,p2)
    #     if i == 0:
    #         sum = sum + valueDict[p1]
    #         print(sum)
    #         break
    #     if valueDict[p2] < valueDict[p1]:
    #         sum = valueDict[p1] - valueDict[p2] + sum
    #     else:
    #         sum = valueDict[p1] + valueDict[p2] + sum
    #     print(sum)

def romanMinimal():
    pass

def charCompare():
    pass

def main():
    test = 'MMMCDLXXXVII'
    test1 = 'XIV'
    #test = list(test1)
    #print(valueDict)
    sum = romanValue(test)
    romanMinimal(sum)
    charCompare()

main()
