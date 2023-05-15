from collections import deque
#test_case = int(input())

for tc in range(1,11):
    aa=int(input())
    l=list(input())

    # {}
    a=deque()
    # []
    b=deque()
    # ()
    ca=deque()
    # <>
    d=deque()
    flag=True
    for c in l:
        if c=="{":
            a.append(c)
        elif c=="}":
            if len(a)>=1:
                a.popleft()
            else:
                flag=False
                break

        if c=="[":
            b.append(c)
        elif c=="]":
            if len(b)>=1:
                b.popleft()
            else:
                flag=False
                break

        if c=="<":
            ca.append(c)
        elif c==">":
            if len(ca)>=1:
                ca.popleft()
            else:
                flag=False
                break

        if c=="(":
            d.append(c)
        elif c==")":
            if len(d)>=1:
                d.popleft()
            else:
                flag=False
                break

    if len(a)>=1 or len(b)>=1 or len(ca)>=1 or len(d)>=1:
        flag=False
    if flag:
        print("#%d %d"%(tc,1))
    else:
        print("#%d %d"%(tc,0))




