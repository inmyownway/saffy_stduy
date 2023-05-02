from collections import deque

def bfs(visited, start):
  q = deque() 
  q.append([0, start, 1, 0])

  while q:
    x, y, i, j = q.popleft() #좌표 x, y, 방향벡터 i, j
    flag = [] #element: 새로운 좌표 nx, ny, 새로운 방향벡터 dx, dy
    
    for dx, dy in [(1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      if nx < 0 or nx > 99 or ny < 0 or ny > 99:
        continue

      if graph[nx][ny] == 2:
        return True
        
      elif graph[nx][ny] == 1 and not visited[nx][ny]:
        #갈림길이 나온 경우, 현재 방향과 다른 방향으로 이동
        if not len(flag) or (i == flag[2] and j == flag[3]):
          flag = [nx, ny, dx, dy]
            
    if len(flag):
      visited[flag[0]][flag[1]] = 1
      q.append(flag)


for _ in range(10):
  test_case = int(input())
  
  graph = []
  for _ in range(100):
    graph.append(list(map(int, input().split())))

  for start in range(100):
    if graph[0][start]:
      visited = [[0]*100 for _ in range(100)]
      visited[0][start] = 1
      res = bfs(visited, start)

    if res:
      print('#{0} {1}'.format(test_case, start))
      break
    
      
     
