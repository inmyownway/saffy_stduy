from collections import deque

direct = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1), (-1, 1)]

def bfs(x, y, p1, p2):
    q = deque()

    # 자신이 놓을 돌과 인접한 곳에 상대편의 돌이 있는 경우, queue에 추가한다
    for d in range(8):
        dx, dy = direct[d]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == p2:
            q.append([nx, ny, d])

    while q:
        x, y, d = q.popleft()
        dx, dy = direct[d]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == p2:
            q.append([nx, ny, d])
            continue

        # 자신의 돌이 있는 경우, 역방향으로 다시 탐색하여 상대편의 돌을 자신의 돌로 만든다
        elif graph[nx][ny] == p1:
            graph[x][y] = p1
            dx, dy = direct[(d+4)%8]

            while True:
                x, y = x + dx, y + dy
                if graph[x][y] == p2:
                    graph[x][y] = p1
                else:
                    break


t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]

    # 처음에 플레이어는 돌을 놓고 시작한다
    x = n//2
    graph[x][x], graph[x-1][x-1] = 2, 2
    graph[x-1][x], graph[x][x-1] = 1, 1

    # 흑, 백이 번갈아가며 돌을 놓는다
    player = [0, 2, 1]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a, b = a-1, b-1

        graph[a][b] = c
        bfs(a, b, c, player[c])

    # 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다
    result = [0, 0]
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                result[0] += 1

            elif graph[i][j] == 2:
                result[1] += 1

    print('#{}'.format(test_case), *result)

