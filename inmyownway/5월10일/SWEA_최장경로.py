

from collections import deque
def dfs(node,d):
    global distance

    if distance < d:
        distance=d
    # [ [2] [1,3] [2] ]
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node]=True
        dfs(next_node,d+1)
        visited[next_node]=False
tc=int(input())
for t in range(1,tc+1):
    n,m=map(int,input().split())
    graph=[[] for _ in range(n+1)]
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)

    visited=[False for _ in range(n+1)]

    distance=0
    for i in range(1,n+1):
        visited[i]=True
        dfs(i,1)
        visited[i]=False


    print("#%d %d"%(t,distance))

