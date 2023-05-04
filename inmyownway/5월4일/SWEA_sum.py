for test in range(1,11):
    n=int(input())
    l=[]
    for i in range(100):
        t=list(map(int,input().split()))
        l.append(t)

    maxNum=-1e9

    for i in range(100):
        maxNum=max(maxNum,sum(l[i]))

    s = 0
    for i in range(100):
        s=0
        for j in range(100):
            s+=l[j][i]
        maxNum=max(maxNum,s)

    s=0
    for i in range(100):
        s+=l[i][i]
    maxNum = max(maxNum, s)
    s=0
    for i in range(100):
        s+=l[i][99-i]
    maxNum = max(maxNum, s)
    print("#{} {}".format(test,maxNum))



