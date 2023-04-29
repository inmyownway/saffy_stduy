#x를 알고 있는 모든 사람을 방문하는 함수
def dfs(x):
  for y in graph[x]:
    if not visited[y]:
      visited[y] = 1
      dfs(y)


t = int(input())

for test_case in range(1, t+1):
  n, m = map(int, input().split())
  visited = [0 for _ in range(n+1)]
  graph = [[] for _ in range(n+1)]

  #무방향 그래프 생성
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  #처음 방문하는 경우, 새로운 무리를 찾은 것
  cnt = 0
  for x in range(1, n+1):
    if not visited[x]:
      visited[x] = 1
      cnt += 1
      dfs(x)

  print('#{0} {1}'.format(test_case, cnt))
