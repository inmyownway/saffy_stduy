test_case = int(input())

for tc in range(1, test_case + 1):

    l=[]

    rook=[]
    for i in range(8):
        temp=list(input())
        for j in range(len(temp)):
            if temp[j]=='O':
                rook.append((i,j))
        l.append(temp)

    flag=True

    if len(rook)>8 or len(rook)<=7:
        flag=False

    for x,y in rook:
        cnt=0
        for i in range(8):
            if l[x][i]=='O':
                cnt+=1
        #print(x,y,cnt)

        for i in range(8):
            if l[i][y]=='O':
                cnt+=1

        if cnt>=3:
            #print("a")
            flag=False
    #print(flag)
    if flag:
        print("#%d %s"%(tc,"yes"))
    elif flag==False:
        print("#%d %s"%(tc,"no"))

