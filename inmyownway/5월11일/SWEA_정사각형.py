from collections import deque
tset_case=int(input())


def bfs(x,y):

    q=deque()
    q.append((x,y))
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    cnt=0
    while q:
        qx,qy=q.popleft()

        for i in range(4):
            nx=qx+dx[i]
            ny=qy+dy[i]

            if 0<=nx<n and 0<=ny<n:
                if l[qx][qy]+1 == l[nx][ny]:
                    q.append((nx,ny))
                    cnt+=1
    return cnt







for tc in range(1,tset_case+1):
    n=int(input())
    l=[]
    for i in range(n):
        t=list(map(int,input().split()))
        l.append(t)


    maxNum=-1
    answer=0

    for i in range(n):
        for j in range(n):
            result = bfs(i, j)
            if maxNum < result:
                maxNum = result
                answer = l[i][j]
            if maxNum == result and answer > l[i][j]:
                answer = l[i][j]
                maxNum = result

    # for i in range(n):
    #     for j in range(n):
    #         count=bfs(i,j)
    #         if count>maxCount:
    #             maxCount=count
    #             answer=l[i][j]
    #         elif maxCount==count and answer>l[i][j]:
    #             answer=l[i][j]
    #             maxCount=count




    print("#%d %d %d"%(tc,answer,maxNum+1))
