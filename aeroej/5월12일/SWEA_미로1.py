from collections import deque

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= 16 or ny < 0 or ny >= 16:
                continue

            if graph[nx][ny] == 3:
                return True

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append([nx, ny])


for _ in range(10):
    test_case = int(input())
    graph = [list(map(int, input())) for _ in range(16)]

    #출발지 탐색 후 방문처리 (1은 벽, 0은 길, 2는 출발점, 3은 도착점)
    for i in range(16):
        for j in range(16):
            if graph[i][j] == 2:
                start = [i, j]
                graph[i][j] = 1

    result = 0
    if bfs(start):
        result = 1

    print('#{} {}'.format(test_case, result))
