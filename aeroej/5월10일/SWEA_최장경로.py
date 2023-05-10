def dfs(v, count):
  global result
  
  visited[v] = 1
  result = max(result, count)
  
  for x in graph[v]:
    if not visited[x]:
      dfs(x, count+1)
      visited[x] = 0


t = int(input())

for test_case in range(1, t+1):
  v, e = map(int, input().split())
  graph = [[] for _ in range(v + 1)]

  for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

  result = 0

  for i in range(1, v + 1):
    visited = [0] * (v+1)
    dfs(i, 1)

  print("#{} {}".format(test_case, result))
  
