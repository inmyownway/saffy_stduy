from collections import deque

test_case=int(input())
for test in range(1,test_case+1):
    l=[]
    for i in range(4):
        temp=list(map(int,input().split()))
        l.append(temp)
    #print(l)
    q=deque()
    #q.append((0,0,str(l[0][0])))
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    answer=set()

    for i in range(4):
        for j in range(4):
            q.append((i,j,str(l[i][j])))

            while q:
                #print(q)
                x,y,s=q.popleft()
                if len(s)==7:
                    answer.add(s)
                    continue

                for z in range(4):
                    nx=x+dx[z]
                    ny=y+dy[z]

                    if 0<=nx<4 and 0<=ny<4 and len(s)<=6:
                        new_s=s+str(l[nx][ny])
                        q.append((nx,ny,new_s))

    #answer=set(answer)
    #print(answer)
    print("#{} {}".format(test,len((answer))))

:wq


