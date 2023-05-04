test_case=int(input())

def get_parent(x):
    if p[x] !=x:
        p[x]=get_parent(p[x])
    return p[x]
def union(x,y):
    a=get_parent(x)
    b=get_parent(y)
    if a>b: p[a]=b
    else:
        p[b]=a
def find(a,b):
    if get_parent(x)==get_parent(y):
        return True
    else:
        return False
for i in range(1,test_case+1):
    v,e=map(int,input().split())

    p=[i for i in range(v+1)]

    edge=[list(map(int,input().split())) for _ in range(e)]

    answer=0
    edge.sort(key=lambda x: -x[2])

    while edge:
        a,b,v=edge.pop()

        if not find(a, b):
            # 부모를 병합한다.
            union(a, b)
            # 정답에 값을 더한다.
            answer += v

        print('#{} {}'.format(t + 1, answer))



