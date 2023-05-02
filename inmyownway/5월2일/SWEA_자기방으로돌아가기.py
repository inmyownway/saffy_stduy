test_case=int(input())

for test in range(1,test_case+1):
    n=int(input())
    room=[]
    cnt=[0]*201
    for i in range(n):
        x,y,=map(int,input().split())
        room.append([x,y])

    for r in room:
        if x>y:
            temp=x
            x=y
            y=x

        p=(r[0]+1)//2
        q=(r[1]+1)//2

        for i in range(p,q+1):
            cnt[i]+=1

        answer=max(cnt)


    print("#{} {}".format(test,answer))

