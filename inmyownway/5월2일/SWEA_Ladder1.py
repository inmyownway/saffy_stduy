for test_case in range(1,11):
    n=int(input())
    l=[]
    for i in range(100):

        t=list(map(int,input().split()))
        l.append(t)
    #print(l)
    for i in range(100):
        #print(i)
        if l[0][i]==1:
            x=0
            y=i
            visited=[[False]*100 for _ in range(100)]
            while True:
                #print(x,y)
                if l[x][y]==2:
                    print("#{} {}".format(test_case,i))
                    break

                if x==99:
                    break


                if y-1>=0  and visited[x][y-1]==False and l[x][y-1]==1:
                        y-=1
                        visited[x][y]=True
                elif y+1<=99  and visited[x][y+1]==False and l[x][y+1]==1:
                        y+=1
                        visited[x][y]=True
                elif x+1 < 100:
                    if visited[x+1][y]==False:
                        x+=1
                        visited[x][y]=True








