


def check(line):
    if len(line)%2==0:
        mid= (len(line)//2)
    else:
        mid=(len(line)//2)

    for i in range(mid):
        if line[i]!=line[len(line)-1-i]:
            return False
    return True

for tc in range(1, 10+ 1):
    n=int(input())


    l=[]
    for i in range(8):
        temp=list(input())
        temp=list(temp)
        l.append(temp)

    cnt=0
    # a b c d e f
    # n = 3
    # i= 0~3
    # 0~3,1~4,2~5,3~6
    for line in l:

        for i in range(len(line)-n+1):
            if check(line[i:i+n]):
                cnt+=1

    for i in range(len(l)):
        temp=[]
        for j in range(len(l)):
            temp.append(l[j][i])
        #print(temp)
        for z in range(len(temp)-n+1):
            if check(temp[z:z+n]):
                #print(cnt)
                cnt+=1

    print("#%d %d"%(tc,cnt))
