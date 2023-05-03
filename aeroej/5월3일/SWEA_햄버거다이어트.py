def dfs(x, target, kcal):
  global point
  
  if x == N:
    return
    
  target, kcal = target + T[x], kcal + K[x]

  #x번째 음식을 선택하는 경우
  if kcal <= L:
    point = max(point, target)
    dfs(x+1, target, kcal)

  #x번째 음식을 선택하지 않는 경우
  dfs(x+1, target - T[x], kcal - K[x])


T = int(input())

for test_case in range(1, T+1):
  N, L = map(int, input().split())
  T, K = [], []

  for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    K.append(b)

  point = 0
  dfs(0, 0, 0) #중복을 허용하지 않는 조합
  print('#{} {}'.format(test_case, point))
