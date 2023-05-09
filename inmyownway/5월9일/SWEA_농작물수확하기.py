
test_case=int(input())

for test_case in range(1,test_case+1):
    n=int(input())
    l=[]
    for i in range(n):
        temp=list(input())
        t=[]
        for j in range(len(temp)):
            t.append(int(temp[j]))
        l.append(t)
    result=0
    p=n//2
    q=p+1
    for i in range(n):

        result += sum(l[i][p:q])
        #print(p,q,i,l[i][p:q])

        if i+1>=(n//2)+1:
            p+=1
            q-=1
        else:
            p-=1
            q+=1
        #print(l[i][p:q])

    print("#%d %d"%(test_case,result))

