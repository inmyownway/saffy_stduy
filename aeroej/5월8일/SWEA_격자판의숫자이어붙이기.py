from collections import deque

def bfs(i, j):
  q = deque()
  q.append([i, j, 1, graph[i][j]])
  
  while q:
    x, y, cnt, num = q.popleft()

    #일곱 자리인 경우
    if cnt > 6:
      numbers.add(num)
      continue

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx, ny = x + dx, y + dy
      
      if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
        continue
        
      q.append([nx, ny, cnt + 1, num + graph[nx][ny]])
      
  
t = int(input())

for test_case in range(1, t+1):
  graph = [list(map(str, input().split())) for _ in range(4)]
  numbers = set()

  #모든 좌표에서 한번씩 출발
  for i in range(4):
    for j in range(4):
      bfs(i, j)

  print('#{} {}'.format(test_case, len(numbers)))
      
