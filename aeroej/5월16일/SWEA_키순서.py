def dfs(x, graph):
    for y in graph[x]:
        if not visited[y]:
            visited[y] = 1
            dfs(y, graph)


t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    m = int(input())

    # 정방향, 역방향 그래프 생성
    forward = [[] for _ in range(n+1)]
    backward = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        forward[a].append(b)
        backward[b].append(a)

    result = 0
    for node in range(1, n+1):
        visited = [0] * (n+1)
        visited[node] = 1

        dfs(node, forward)
        dfs(node, backward)

        # 모든 노드를 방문한 경우
        if sum(visited) == n:
            result += 1

    print('#{} {}'.format(test_case, result))
