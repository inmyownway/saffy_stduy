from itertools import combinations
test_case=int(input())

for test in range(1,test_case+1):
    n,maxC=map(int,input().split())

    l=[]

    answer=-1e9
    for i in range(n):
        score,cal=map(int,input().split())
        l.append((score,cal))

    for i in range(1,n+1):

        temp=list(combinations(l,i))
        #print(temp)
        sumScore=0
        sumCal=0
        for t in temp:
            for j in range(len(t)):
                sumScore=t[j][0]
                sumCal=t[j][1]
            if sumCal > maxC:
                continue
            if answer<sumScore:
                print(sumScore,sumCal)
                answer=sumScore


    print("#{} {}".format(test,answer))






