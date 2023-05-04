for _ in range(10):
  test_case = int(input())
  
  graph = []
  for _ in range(100):
    graph.append(list(map(int, input().split())))

  diag = [0, 0]
  ans = 0
  
  for i in range(100):
    #각 행의 합
    ans = max(ans, sum(graph[i]))
    
    for j in range(100):
      #각 대각선의 합
      if i == j:
        diag[0] += graph[i][j]
      elif i + j == 99:
        diag[1] += graph[i][j]

      #각 열의 합
      if i == 0:
        break
      graph[0][j] += graph[i][j]

  #각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값
  ans = max(ans, max(graph[0]), max(diag))
  print('#{} {}'.format(test_case, ans))
    
    
