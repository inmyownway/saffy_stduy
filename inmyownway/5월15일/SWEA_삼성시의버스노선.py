test_case=int(input())
for tc in range(1,test_case+1):
    t=int(input())



    busstop=[0 for _ in range(5001)]
    possible=[False for _ in range(5001)]
    bus=[]
    for i in range(t):
        a,b,=map(int,input().split())
        bus.append((a,b))

    # 1 2 2 3 2 2 2 2 1 0
    pstop=[]
    p=int(input())
    for i in range(p):
        temp=int(input())
        pstop.append(temp)
        possible[temp]=True

    for x,y in bus:

        for i in range(x,y+1):
            if possible[i]==True:
                busstop[i]+=1

    answer=[]
    for i in pstop:
        answer.append(busstop[i])

    print("#%d"%(tc),*answer)




