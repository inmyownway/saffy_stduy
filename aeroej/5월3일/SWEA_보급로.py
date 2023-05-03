import heapq

def bfs(n):
  q = []
  heapq.heappush(q, [0, 0, 0]) #우선순위 큐
  
  while q:
    cost, x, y = heapq.heappop(q)

    #상하좌우 이동
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy

      #목적지 도달
      if nx == n-1 and ny == n-1:
        return cost
        
      #그래프를 벗어난 경우
      elif nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
        continue

      #처음 방문한 경우
      elif not visited[nx][ny]:
        visited[nx][ny] = 1
        heapq.heappush(q, [cost + graph[nx][ny], nx, ny])
        

c = int(input())

for test_case in range(1, c+1):
  n = int(input())
  visited = [[0]*n for _ in range(n)]
  
  graph = []
  for _ in range(n):
    graph.append(list(map(int, input())))

  print('#{0} {1}'.format(test_case, bfs(n)))
