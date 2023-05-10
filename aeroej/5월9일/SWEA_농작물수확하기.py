t = int(input())

for test_case in range(1, t+1):
  n = int(input())
  graph = [list(map(int, input())) for _ in range(n)]
  ans = 0
  
  for i in range(n):
    diff = abs(i - n//2)
    
    for j in range(diff, n-diff):
      ans += graph[i][j]

  print('#{} {}'.format(test_case, ans))
      
