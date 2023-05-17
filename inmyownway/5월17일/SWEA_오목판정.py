from collections import deque
def check(ii,jj):

    c=0
    while c<8:
        #print("c",c)
        #print(c)
        #print()
        dx=[-1,1,0,0,-1,1,-1,1]
        dy=[0,0,-1,1,-1,1,1,-1]

        q=deque()
        q.append((ii,jj))
        #print(q)
        cnt=1
        visited=[[False]*n for _ in range(n)]

        while q:
            x,y=q.popleft()

            visited[x][y]=True
            for i in range(2):
                #rint(dx[i+c],dy[i+c])
                nx=x+dx[i+c]
                ny=y+dy[i+c]
               # print("dx,dy",dx[i+c],dy[i+c])
                #p#rint(nx,ny)

                if 0<=nx <n and 0<=ny <n:
                    if visited[nx][ny]==False and board[nx][ny]=='o':
                        q.append((nx,ny))
                        visited[nx][ny]=True
                        cnt+=1

            if cnt>=5:
                return True
        c+=2
    return False



for tc in range(int(input())):
        n=int(input())

        board=[]
        for i in range(n):
            l=list(input())
            board.append(l)

        flag=False
        for i in range(n):
            for j in range(n):
                if board[i][j]=='o':
                    if check(i,j):
                        flag= True
                        break
            if flag==True:
                break
        if flag:
            print("#%d %s" % (tc + 1, "YES"))
        else:
            print("#%d %s" % (tc + 1, "NO"))



