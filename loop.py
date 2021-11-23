num =1
numAll =0
while num <101:
    if num % 2 == 1:
        print(num)
        numAll=num+numAll
    num += 1
    print(numAll)