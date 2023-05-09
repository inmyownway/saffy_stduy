from collections import deque
for test_case in range(1,11):
    t=int(input())
    l=list(map(int,input().split()))
    l=deque(l)
    cycle=1
    while True:

        x=l.popleft()

        if cycle==6:
            cycle=1
        x-=cycle

        if x<=0:
            x=0
            l.append(x)
            break
        else:
            l.append(x)
        cycle+=1

    #l=list(l)
    #print(l)
    #print("#{} {}".format(test_case,l.join))
    print("#%d %d %d %d %d %d %d %d %d" %(test_case,l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7]))

