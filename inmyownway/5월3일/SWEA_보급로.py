from collections import deque
test_case=int(input())
for test in range(1,test_case+1):
    n=int(input())
    l=[]
    for i in range(n):
        temp=list(input())
        t=[]
        for j in temp:
            t.append(int(j))
        l.append(t)

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    q=deque()
    q.append((0,0))
    visited=[[False]*n for _ in range(n)]
    keys=[[99999]*n for _ in range(n)]
    keys[0][0]=0
    while q:

        x,y=q.popleft()
        #visited[x][y]=True
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < n and 0<= ny <n:
                if keys[x][y]+ l[nx][ny] < keys[nx][ny]:
                    keys[nx][ny]=keys[x][y]+l[nx][ny]

                    q.append((nx,ny))

    # for i in keys:
    #     print(i)
    # print()
    print("#{} {}".format(test,keys[-1][-1]))







