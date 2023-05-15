from collections import deque
for tc in range(1,11):

    t=int(input())

    l=[]
    for i in range(16):
        t=list(input())
        temp=[]
        for j in t:
            temp.append(int(j))
        l.append(temp)

    visited=[[False]*16 for _ in range(16)]

    q=deque()

    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    q.append((1,1))
    flag=False
    while q:
        x,y=q.popleft()

        if l[x][y]==3:

            flag=True
            break
        visited[x][y]=True

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #print("nx,ny",nx,ny,l[nx][ny],visited[nx][ny])

            if 0<= nx <16 and 0<=ny<16:

                if l[nx][ny]!=1:

                    if visited[nx][ny]==False:
                        q.append((nx,ny))
                        visited[nx][ny]=True


    #print(flag)
    if flag:

        print("#%d %d" %(tc,1))
    else:
        print("#%d %d"%(tc,0))

